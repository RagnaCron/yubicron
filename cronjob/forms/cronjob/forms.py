from django import forms


class TitleForm(forms.Form):
	title = forms.CharField(max_length=30, label_suffix=' ', initial='Title...')
	url = forms.URLField(label_suffix=' ', initial='http://')


class AuthenticateForm(forms.Form):
	box = forms.BooleanField(required=False)
	username = forms.CharField(max_length=30, required=False,
	                           label_suffix=' ', label='Username')
	password = forms.CharField(max_length=20, widget=forms.PasswordInput,
	                           required=False, label='Password',
	                           label_suffix=' ')


MINUTES = ((str(x), str(x)) for x in range(0, 60))
HOURS = ((str(x), str(x)) for x in range(0, 24))
DAYS = ((str(x), str(x)) for x in range(1, 32))


class MinutesForm(forms.Form):
	times = forms.ChoiceField(choices=MINUTES, label='Every',
	                          label_suffix=' ', required=False)


class HoursFrom(forms.Form):
	times = forms.ChoiceField(choices=HOURS, label='',
	                          label_suffix=' ', required=False)


class DaysFrom(forms.Form):
	times = forms.ChoiceField(choices=DAYS, label='', initial=1,
	                          label_suffix=' ', required=False)


class UserMessageForm(forms.Form):
	failedJob = forms.BooleanField(required=False, label_suffix=' ')
	successfulJob = forms.BooleanField(required=False, label_suffix=' ')
	stopJob = forms.BooleanField(required=False)


class GeneralForm(forms.Form):
	willSaveMessage = forms.BooleanField(required=False, label_suffix=' ')
