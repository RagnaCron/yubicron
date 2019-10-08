from django.shortcuts import render

# Create your views here.


def index(request):
	context = {}
	# TODO: - POST evaluation -> create model entry to CronJob
	return render(request, 'cronjob/index.html', context)
