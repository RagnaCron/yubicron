from django import forms
from django.core.exceptions import ValidationError


class CronLoginForm(forms.Form):
	username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
	password = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
	yubicron = forms.CharField(label='Yubikey', widget=forms.PasswordInput, label_suffix='', max_length=44)

	def clean_yubicron(self):
		yubicron = self.cleaned_data['yubicron']
		if len(yubicron) < 44:
			raise ValidationError("Press your yubikey for all 44 chars")
		return yubicron

	def valid_yubi(self):
		yubi = YubiKeyModel.yubi_key
		if self.clean_yubicron()[:12] == yubi:
			return yubi
		raise ValidationError("Enter 'your' Yubikey.")
