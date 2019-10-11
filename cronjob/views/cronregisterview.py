from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from cronjob.forms.cronjob.cronusercreationform import MyUserCreationForm


def userRegistration(request):
	if request.method == 'POST':
		user_creation_form = MyUserCreationForm(request.POST)
		if user_creation_form.is_valid():
			user_creation_form.save()
			auth.login(request, user=User.objects.get(username=user_creation_form.cleaned_data['username']))
			return render(request, 'cronjob/cronhome.html', {'message': 'Successful User Signup.'})
	else:
		user_creation_form = MyUserCreationForm()
	context = {'user_creation_form': user_creation_form, 'errors': user_creation_form.errors}
	return render(request, 'cronjob/cronregisteruser.html', context)
