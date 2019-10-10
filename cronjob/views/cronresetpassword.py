from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from cronjob.forms.cronjob.cronresetpasswordform import ResetPasswordForm


def resetPassword(request):
	if request.method == 'POST':
		reset_password = ResetPasswordForm(request.POST)
		if reset_password.is_valid():

			return render_to_response('cronjob/cronhome.html', {'message': 'Email was Posted.'})
	else:
		reset_password = ResetPasswordForm()
	context = {'reset_password': reset_password, }
	return render(request, 'cronjob/cronresetpassword.html', context)
