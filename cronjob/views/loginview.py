from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def userLogin(request):
	context = {}
	# if request.method == 'POST':
	# 	username = request.POST['username']
	# 	password = request.POST['password']
	# 	user = authenticate(request, username=username, password=password)
	# 	if user is not None:
	# 		login(request, user)
	# 		return redirect('cronjob:home')
	# 	else:
	# 		context = {'error': 'Try again.'}
	return render(request, 'cronjob/cronuserlogin.html', context=context)