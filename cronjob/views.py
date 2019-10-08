from django.shortcuts import render
from cronjob.forms.cronjob.forms import AuthenticateForm, TitleForm
from cronjob.models import CronJob

# Create your views here.


def createCronJob(request):
	# TODO: - POST evaluation -> create model entry to CronJob
	title = TitleForm()
	authenticate = AuthenticateForm()
	context = {'title': title, 'authenticate': authenticate}
	if request.method == 'POST':
		cronJob = CronJob()
		title = TitleForm(request.POST)
		authenticate = AuthenticateForm(request.POST)
		times = request.POST.getlist('times')
		messages = request.POST.getlist('messages')
		if not messages.isEmpty():
			for m in messages:
				if m == 0:
					cronJob.failMessage = True
				if m == 1:
					cronJob.successMessage = True
				if m == 2:
					cronJob.automaticJobStopperWhenToManyFailures = True
		if not times.isEmpty():
			pass


	return render(request, 'cronjob/cronjob.html', context)


def isCheckbox(Bool):
	pass
