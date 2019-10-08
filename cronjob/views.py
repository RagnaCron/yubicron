from django.shortcuts import render

# Create your views here.


def index(request):
	# TODO: - POST
	return render(request, 'cronjob/index.html', {})
