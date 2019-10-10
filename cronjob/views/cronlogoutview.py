from django.contrib.auth import logout
from django.shortcuts import redirect


def userLogout(request):
	logout(request)
	return redirect('cronjob:home')
