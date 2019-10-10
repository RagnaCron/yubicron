from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from cronjob.forms.cronjob.cronloginform import CronLoginForm


def userLogin(request):
	website_title = 'Cron Login'

	if request.method == 'POST':
		user_login = CronLoginForm(request.POST)
		if user_login.is_valid():
			username = user_login.cleaned_data.get('username')
			password = user_login.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('cronjob:home')
	else:
		user_login = CronLoginForm()
	context = {'website_title': website_title, 'user_login': user_login, }
	return render(request, 'cronjob/cronuserlogin.html', context=context)
