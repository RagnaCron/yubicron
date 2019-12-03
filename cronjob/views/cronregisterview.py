from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from yubico_client import Yubico

from cronjob.forms.cronjob.cronusercreationform import MyUserCreationForm


def userRegistration(request):
	client = Yubico('50927', 'VNiJHml4DqqTjQFeu5yvrbtM97U=')
	if request.method == 'POST':
		user_creation_form = MyUserCreationForm(request.POST)
		if user_creation_form.is_valid():

			if client.verify(user_creation_form.clean_yubicron()):

				user_creation_form.save()
				auth.login(request, user=User.objects.get(username=user_creation_form.cleaned_data['username']))
				return render(request, 'cronjob/cronhome.html', {'message': 'Successful User Signup.'})
	else:
		user_creation_form = MyUserCreationForm()
	context = {'user_creation_form': user_creation_form, 'errors': user_creation_form.errors}
	return render(request, 'cronjob/cronregisteruser.html', context)
