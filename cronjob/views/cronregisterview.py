from django.core.checks import messages
from django.shortcuts import render, redirect
from cronjob.forms.cronjob.cronusercreationform import MyUserCreationForm


def register(request):
	website_title = 'Cron Register'

	if request.method == 'POST':
		user_creation_form = MyUserCreationForm(request.POST)
		if user_creation_form.is_valid():
			user_creation_form.save()
			return redirect('cronjob:createCronJob')

	else:
		user_creation_form = MyUserCreationForm()

	context = {'website_title': website_title, 'user_creation_form': user_creation_form}
	return render(request, 'cronjob/cronregisteruser.html', context)
