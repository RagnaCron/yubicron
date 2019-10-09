from django.shortcuts import render
from cronjob.forms.cronjob.forms import AuthenticateForm, TitleForm, UserMessageForm, GeneralForm, TimesForm


# Create your views here.


def createCronJob(request):
	# TODO: - POST evaluation -> create model entry to CronJob
	context = renderCronJob(None)
	if request.method == 'POST':
		title = TitleForm(data=request.POST)
		authenticate = AuthenticateForm(data=request.POST)
		userMessage = UserMessageForm(data=request.POST)
		minutes = request.POST.get('minutes')
		times = TimesForm(data=request.POST)
		general = GeneralForm(data=request.POST)
		executionTime = calcSchedule(request, times)
		print(executionTime)
		return render(request, 'cronjob/cronjob.html', {'title': title, 'authenticate': authenticate, 'times': times,
		                                                'minutes': minutes, 'userMessage': userMessage,
		                                                'general': general})

	return render(request, 'cronjob/cronjob.html', context)


def renderCronJob(request):
	title = TitleForm(data=request)
	authenticate = AuthenticateForm(data=request)
	userMessage = UserMessageForm(data=request)
	times = TimesForm(data=request)
	general = GeneralForm(data=request)

	context = {'title': title, 'authenticate': authenticate, 'times': times,
	           'userMessage': userMessage, 'general': general}
	return context


# Original Gangster Programmer (OGP) of calcSchedule(request): Vincenz Gregori
# OGP changer: Manuel Werder
def calcSchedule(request, times):
	if request.POST.get('id_times') == 'minutes':
		return '*/' + str(times['minutes'].value()) + ' * * * *'
	elif request.POST.get('id_times') == 'hours':
		return str(times['minutes'].value()) + ' ' + str(times['hours'].value()) + ' * * *'
	elif request.POST.get('id_times') == 'days':
		return str(times['minutes'].value()) + ' ' + str(times['hours'].value()) + ' ' + str(times['days'].value()) + ' * *'
	elif request.POST.get('id_times') == 'userDefined':
		return '* * * * *'
