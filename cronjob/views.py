from django.shortcuts import render
from cronjob.forms.cronjob.forms import AuthenticateForm, TitleForm, UserMessageForm, GeneralForm
from cronjob.forms.cronjob.forms import MinutesForm, HoursFrom, DaysFrom
from cronjob.models import CronJob


# Create your views here.


def createCronJob(request):
	# TODO: - POST evaluation -> create model entry to CronJob
	if request.method == 'POST':
		# title = TitleForm(data=request.POST)
		# authenticate = AuthenticateForm(data=request.POST)
		# userMessage = UserMessageForm(data=request.POST)
		# minutes = MinutesForm(data=request.POST)
		# hours = HoursFrom(data=request.POST)
		# days = DaysFrom(data=request.POST)
		# general = GeneralForm(data=request.POST)
		#
		# context = {'title': title, 'authenticate': authenticate,
		#            'minutes': minutes, 'hours': hours, 'days': days,
		#            'userMessage': userMessage, 'general': general}
		context = renderCronJob(request.POST)
		cleanData = cleanedPOSTRequests(context)
		# title = cleanData['title']['title']
		# url = cleanData['title']['url']
		# authenticate = cleanData['authenticate']['box']
		# username = cleanData['authenticate']['username']
		# password = cleanData['authenticate']['password']
		executionTime = calcSchedule(request, cleanData)
		print(executionTime)
		print(cleanData)
		# string = 'exe {0}, title: {1}, url: {2}, auth: {3}, username: {4}, password: {5}'\
		# 	.format(executionTime, title, url, authenticate, username, password)
		# print(string)


	else:
		context = renderCronJob(None)
	return render(request, 'cronjob/cronjob.html', context)


def validData(data):
	return data.is_valid()


def cleanedPOSTRequests(context):
	newContext = {}
	for key in context.keys():
		if context[key].is_valid():
			newContext[key] = context[key].cleaned_data
	return newContext


def renderCronJob(request):
	title = TitleForm(data=request)
	authenticate = AuthenticateForm(data=request)
	userMessage = UserMessageForm(data=request)
	minutes = MinutesForm(data=request)
	hours = HoursFrom(data=request)
	days = DaysFrom(data=request)
	general = GeneralForm(data=request)

	context = {'title': title, 'authenticate': authenticate,
	           'minutes': minutes, 'hours': hours, 'days': days,
	           'userMessage': userMessage, 'general': general}
	return context


# Original Gangster Programmer (OGP) of calcSchedule(request): Vincenz Gregori
# OGP changer: Manuel Werder
def calcSchedule(request, cleanData):
	if request.POST.get('id_times') == 'minutes':
		minutes = cleanData['minutes']['times']
		return '*/' + str(minutes) + ' * * * *'
	elif request.POST.get('id_times') == 'hours':
		minutes = cleanData['minutes']['times']
		hours = cleanData['hours']['times']
		return str(minutes) + ' ' + str(hours) + ' * * *'
	elif request.POST.get('id_times') == 'days':
		minutes = cleanData['minutes']['times']
		hours = cleanData['hours']['times']
		days = cleanData['days']['times']
		return str(minutes) + ' ' + str(hours) + ' ' + str(days) + ' * *'
	elif request.POST.get('id_times') == 'userDefined':
		return '* * * * *'


# Original Gangster Programmer of checkCheckbox(cb): Vincenz Gregori
def checkCheckbox(cb):
	return cb == 'True'


# if title.is_valid():
# 	data = title.cleaned_data
# 	print(data)
# if authenticate.is_valid():
# 	data = authenticate.cleaned_data
# 	print(data)
# if minutes.is_valid():
# 	data = minutes.cleaned_data
# 	print(data)
# if hours.is_valid():
# 	data = hours.cleaned_data
# 	print(data)
# if days.is_valid():
# 	data = hours.cleaned_data
# 	print(data)
# if userMessage.is_valid():
# 	data = userMessage.cleaned_data
# 	print(data)
# if general.is_valid():
# 	data = general.cleaned_data
# 	print(data)
