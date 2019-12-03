from django.contrib.auth import login, authenticate
from django.shortcuts import render
from cronjob.forms.cronjob.cronloginform import CronLoginForm


def userLogin(request):
	if request.method == 'POST':
		user_login = CronLoginForm(request.POST)
		# todo: otp yubikey
		if user_login.is_valid():
			username = user_login.cleaned_data.get('username')
			password = user_login.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return render(request, 'cronjob/cronhome.html', {'message': 'Your login was successful.'})
			error = 'Username or Password wrong.'
		else:
			error = user_login.errors
	else:
		user_login = CronLoginForm()
		error = user_login.errors
	context = {'user_login': user_login, 'error': error, }
	return render(request, 'cronjob/cronuserlogin.html', context=context)
