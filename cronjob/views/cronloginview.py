from django.contrib.auth import login, authenticate
from django.shortcuts import render
from yubico_client import Yubico
from yubico_client.yubico_exceptions import StatusCodeError

from cronjob.forms.cronjob.cronloginform import CronLoginForm


def userLogin(request):
	client = Yubico('50927', 'VNiJHml4DqqTjQFeu5yvrbtM97U=')
	error = ''
	if request.method == 'POST':
		user_login = CronLoginForm(request.POST)
		if user_login.is_valid():
			username = user_login.cleaned_data.get('username')
			password = user_login.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				try:
					client.verify(user_login.clean_yubicron())
					# toto: login error
					login(request, user)
					return render(request, 'cronjob/cronhome.html', {'message': 'Your login was successful.'})
				except StatusCodeError:
					error = 'Username, Password or Yubikey wrong.'
		else:
			error = user_login.errors
	else:
		user_login = CronLoginForm()
		error = user_login.errors
	context = {'user_login': user_login, 'error': error, }
	return render(request, 'cronjob/cronuserlogin.html', context=context)
