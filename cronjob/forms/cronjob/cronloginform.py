from django import forms


class CronLoginForm(forms.Form):
	username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
	password = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
	yubicron = forms.CharField(label='Yubikey', widget=forms.PasswordInput, label_suffix='', max_length=44)
