from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from cronjob.forms.cronjob.cronjobforms import AuthenticateForm, TitleForm, UserMessageForm, GeneralForm
from cronjob.forms.cronjob.cronjobforms import MinutesForm, HoursFrom, DaysFrom, UserDefinedTimeForm
from cronjob.models import CronJob


# Create your views here.


@login_required(redirect_field_name='userLogin', login_url='/login')
def createCronJob(request):
	website_title = 'Create Cron Job'
	# TODO: - POST evaluation -> create model entry to CronJob
	title = TitleForm(data=request.POST or None)
	authenticate = AuthenticateForm(data=request.POST or None)
	minutes = MinutesForm(data=request.POST or None)
	hours = HoursFrom(data=request.POST or None)
	days = DaysFrom(data=request.POST or None)
	user_defined = UserDefinedTimeForm(data=request.POST or None)
	user_message = UserMessageForm(data=request.POST or None)
	general = GeneralForm(data=request.POST or None)
	context = {'website_title': website_title, 'title': title, 'authenticate': authenticate,
	           'minutes': minutes, 'hours': hours, 'days': days, 'user_defined': user_defined,
	           'user_message': user_message, 'general': general}
	if request.method == 'POST':
		execution_time = calcSchedule(request, minutes, hours, days, user_defined)
		cron_job = CronJob(
			user=auth.get_user(request),
			title=title['title'].value(),
			url=title['url'].value(),
			needs_authentication=authenticate['box'].value(),
			username=authenticate['username'].value(),
			password=authenticate['password'].value(),
			execution_time=execution_time,
			fail_message=user_message['failed_job'].value(),
			success_message=user_message['successful_job'].value(),
			automatic_job_stopper_when_to_many_failures=user_message['stop_job'].value(),
			will_save_message=general['will_save_message'].value()
		)
		cron_job.save()
		return redirect('cronjob:home')

	return render(request, 'cronjob/cronjob.html', context)


# Original Gangster Programmer (OGP) of calcSchedule(request): Vincenz Gregori
# OGP changer: Manuel Werder
def calcSchedule(request, minutes, hours, days, user_defined):
	if request.POST.get('id_times') == 'minutes':
		return '*/' + str(minutes['each_minute'].value()) + ' * * * *'
	elif request.POST.get('id_times') == 'hours':
		return str(hours['every_minute'].value()) + \
		       ' ' + str(hours['every_hour'].value()) + ' * * *'
	elif request.POST.get('id_times') == 'days':
		return str(days['every_minute_day'].value()) + \
		       ' ' + str(days['every_hours_day'].value()) + \
		       ' ' + str(days['every_month_day'].value()) + ' * *'
	elif request.POST.get('id_times') == 'user_defined':
		return str(user_defined['user_defined'].value())
