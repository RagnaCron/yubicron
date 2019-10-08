from django.shortcuts import render
from cronjob.forms.cronjob.forms import AuthenticateForm, TitleForm, UserMessageForm, GeneralForm, MinutesForm
from cronjob.models import CronJob


# Create your views here.


def createCronJob(request):
	# TODO: - POST evaluation -> create model entry to CronJob
	title = TitleForm(request.POST or None)
	authenticate = AuthenticateForm(request.POST or None)
	userMessage = UserMessageForm(request.POST or None)
	minutes = MinutesForm(request.POST or None)
	general = GeneralForm(request.POST or None)
	context = {'title': title, 'authenticate': authenticate,
	           'minutes': minutes, 'userMessage': userMessage,
	           'general': general}
	# if request.method == 'POST':
	# 	cronJob = CronJob()

	return render(request, 'cronjob/cronjob.html', context)
