from django.shortcuts import render


def home(request):
	return render(request, 'cronjob/cronhome.html', {'message': ''})
