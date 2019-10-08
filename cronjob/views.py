from django.shortcuts import render

# Create your views here.
from cronjob.forms.cronjob.forms import Authenticate


def index(request):
	# TODO: - POST evaluation -> create model entry to CronJob
	form = Authenticate(request.POST or None)
	context = { 'form': form, }
	if request.method is 'POST':
		if form.is_valid():
			print("Hello")

	return render(request, 'cronjob/index.html', context)
