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


class MinutesForm(forms.Form):
	minutes = forms.IntegerField(min_value=0, max_value=59, label='Every', label_suffix=' ', required=False)


class HoursFrom(forms.Form):
	hours = forms.IntegerField(min_value=0, max_value=23, label_suffix=' ', required=False)
	minutes = forms.IntegerField(min_value=0, max_value=59, label_suffix=' ', required=False)


class DaysFrom(forms.Form):
	days = forms.IntegerField(min_value=1, max_value=31, label_suffix=' ', required=False)
	hours = forms.IntegerField(min_value=0, max_value=23, label_suffix=' ', required=False)
	minutes = forms.IntegerField(min_value=0, max_value=59, label_suffix=' ', required=False)


class UserMessageForm(forms.Form):
	failedJob = forms.BooleanField(required=False, label_suffix=' ')
	successfulJob = forms.BooleanField(required=False, label_suffix=' ')
	stopJob = forms.BooleanField(required=False)


class GeneralForm(forms.Form):
	willSaveMessage = forms.BooleanField(required=False, label_suffix=' ')
