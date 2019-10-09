from django.shortcuts import render
from cronjob.forms.cronjob.forms import AuthenticateForm, TitleForm, UserMessageForm, GeneralForm
from cronjob.forms.cronjob.forms import MinutesForm, HoursFrom, DaysFrom, MonthsFrom
from cronjob.models import CronJob


# Create your views here.


def createCronJob(request):
	# TODO: - POST evaluation -> create model entry to CronJob
	title = TitleForm(request.POST or None)
	authenticate = AuthenticateForm(request.POST or None)
	userMessage = UserMessageForm(request.POST or None)
	minutes = MinutesForm(request.POST or None)
	hours = HoursFrom(request.POST or None)
	days = DaysFrom(request.POST or None)
	months = DaysFrom(request.POST or None)
	general = GeneralForm(request.POST or None)

	context = {'title': title, 'authenticate': authenticate,
	           'minutes': minutes, 'hours': hours,
	           'days': days, 'months': months,
	           'userMessage': userMessage, 'general': general}
	# if request.method == 'POST':
	# 	cronJob = CronJob()

	return render(request, 'cronjob/cronjob.html', context)


# Original Gangster Programmer of calcSchedule(request): Vincenz Gregori
def calcSchedule(request):
	if request.POST.get("rb", "") == "1":
		rv = "*/" + request.POST.get("Minute1", "") + " * * * *"
		return rv
	elif request.POST.get("rb", "") == "2":
		rv = request.POST.get("Minute2", "") + " " + request.POST.get("Hour2", "") + " * * *"
		return rv
	elif request.POST.get("rb", "") == "3":
		rv = request.POST.get("Minute3", "") + " " + request.POST.get("Hour3", "") + " " + request.POST.get("Day3",
                                                                                              "") + " * *"
		return rv
	elif request.POST.get("rb", "") == "4":
		rv = request.POST.get("Hour3", "")
		return rv


# Original Gangster Programmer of checkCheckbox(cb): Vincenz Gregori
def checkCheckbox(cb):
	return cb == 'True'
