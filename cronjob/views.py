from django.shortcuts import render
from cronjob.forms.cronjob.forms import AuthenticateForm, TitleForm, UserMessageForm, GeneralForm
from cronjob.forms.cronjob.forms import MinutesForm, HoursFrom, DaysFrom
from cronjob.models import CronJob


# Create your views here.


def createCronJob(request):
	# TODO: - POST evaluation -> create model entry to CronJob
	context = {}
	if request.method == 'POST':
		context = renderCronJob(request.POST)
		cleanData = cleanedPOSTRequests(context)
		title = cleanData['title']['title']
		url = cleanData['title']['url']
		authenticate = cleanData['authenticate']['box']
		username = cleanData['authenticate']['username']
		password = cleanData['authenticate']['password']
		executionTime = calcSchedule(request, cleanData)
		print(executionTime)
		print(cleanData)
		# string = 'exe {0}, title: {1}, url: {2}, auth: {3}, username: {4}, password: {5}'\
		# 	.format(executionTime, title, url, authenticate, username, password)
		# print(string)
	else:
		context = renderCronJob(None)
	return render(request, 'cronjob/cronjob.html', context)


def cleanedPOSTRequests(context):
	newContext = {}
	for key in context.keys():
		if context[key].is_valid():
			newContext[key] = context[key].cleaned_data
	return newContext


def renderCronJob(request):
	title = TitleForm(request)
	authenticate = AuthenticateForm(request)
	userMessage = UserMessageForm(request)
	minutes = MinutesForm(request)
	hours = HoursFrom(request)
	days = DaysFrom(request)
	general = GeneralForm(request)

	context = {'title': title, 'authenticate': authenticate,
	           'minutes': minutes, 'hours': hours, 'days': days,
	           'userMessage': userMessage, 'general': general}
	return context


# Original Gangster Programmer (OGP) of calcSchedule(request): Vincenz Gregori
# OGP changer: Manuel Werder
def calcSchedule(request, cleanData):
	if request.POST.get('id_times') == 'minutes':
		minutes = cleanData['minutes']['times']
		return minutes + ' * * * *'
	elif request.POST.get('id_times') == 'hours':
		minutes = cleanData['minutes']['times']
		hours = cleanData['hours']['times']
		return minutes + ' ' + hours + ' * * *'
	elif request.POST.get('id_times') == 'days':
		minutes = cleanData['minutes']['times']
		hours = cleanData['hours']['times']
		days = cleanData['days']['times']
		return minutes + ' ' + hours + ' ' + days + ' * *'
	elif request.POST.get('id_times') == 'userDefined':
		return '* * * * *'


# Original Gangster Programmer of checkCheckbox(cb): Vincenz Gregori
def checkCheckbox(cb):
	return cb == 'True'
