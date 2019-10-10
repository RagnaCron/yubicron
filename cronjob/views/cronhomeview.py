from django.shortcuts import render


def home(request):
	website_title = 'Cron Home'
	return render(request, 'cronjob/cronhome.html', {'website_title': website_title, 'message': ''})
