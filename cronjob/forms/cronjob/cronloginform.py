from django import forms
from django.contrib import auth


class CronLoginForm(forms.Form):
	username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
	password = forms.CharField(label='Enter password', widget=forms.PasswordInput)
