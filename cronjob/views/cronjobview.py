from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cronjob.forms.cronjob.cronjobforms import AuthenticateForm, TitleForm, UserMessageForm, GeneralForm
from cronjob.forms.cronjob.cronjobforms import MinutesForm, HoursFrom, DaysFrom


# Create your views here.

# @login_required(redirect_field_name='login', login_url='/login')
def createCronJob(request):
	# TODO: - POST evaluation -> create model entry to CronJob
	context = renderCronJob(None)
	if request.method == 'POST':
		title = TitleForm(data=request.POST)
		authenticate = AuthenticateForm(data=request.POST)
		user_message = UserMessageForm(data=request.POST)
		minutes = MinutesForm(data=request.POST)
		hours = HoursFrom(data=request.POST)
		days = DaysFrom(data=request.POST)
		general = GeneralForm(data=request.POST)
		execution_time = calcSchedule(request, minutes, hours, days)
		context = {'title': title, 'authenticate': authenticate,
		           'minutes': minutes, 'hours': hours, 'days': days,
		           'userMessage': user_message, 'general': general}
		return render(request, 'cronjob/cronjob.html', context)

	return render(request, 'cronjob/cronjob.html', context)


def renderCronJob(request):
	title = TitleForm(data=request)
	authenticate = AuthenticateForm(data=request)
	user_message = UserMessageForm(data=request)
	minutes = MinutesForm(data=request)
	hours = HoursFrom(data=request)
	days = DaysFrom(data=request)
	general = GeneralForm(data=request)

	context = {'title': title, 'authenticate': authenticate, 'minutes': minutes,
	           'hours': hours, 'days': days,
	           'user_essage': user_message, 'general': general}
	return context


# Original Gangster Programmer (OGP) of calcSchedule(request): Vincenz Gregori
# OGP changer: Manuel Werder
def calcSchedule(request, minutes, hours, days):
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
		return '* * * * *'
