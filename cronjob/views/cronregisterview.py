from django.shortcuts import render, redirect, render_to_response
from cronjob.forms.cronjob.cronusercreationform import MyUserCreationForm


def register(request):
	website_title = 'Cron Signup'

	if request.method == 'POST':
		user_creation_form = MyUserCreationForm(request.POST)
		if user_creation_form.is_valid():
			user_creation_form.save()
			return render_to_response('cronjob/cronhome.html', {'message', 'Successful User Signup.'})
	else:
		user_creation_form = MyUserCreationForm()

	errors = user_creation_form.errors
	context = {'website_title': website_title, 'user_creation_form': user_creation_form, 'errors': errors}
	return render(request, 'cronjob/cronregisteruser.html', context)
