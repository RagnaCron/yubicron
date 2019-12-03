from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from django.shortcuts import render
from yubico_client import Yubico
from yubico_client.yubico_exceptions import StatusCodeError, SignatureVerificationError, InvalidClientIdError

from cronjob.forms.cronjob.cronloginform import CronLoginForm


# noinspection PyBroadException
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
					user_login.valid_yubi()
					try:
						client.verify(user_login.clean_yubicron())
						login(request, user)
						return render(request, 'cronjob/cronhome.html', {'message': 'Your login was successful.'})
					except Exception:
						error = 'Wrong Yubikey'
				except ValidationError as er:
					error = er
			else:
				error = 'Wrong username or password'

		else:
			error = user_login.errors
	else:
		user_login = CronLoginForm()
		error = user_login.errors
	context = {'user_login': user_login, 'error': error, }
	return render(request, 'cronjob/cronuserlogin.html', context=context)
