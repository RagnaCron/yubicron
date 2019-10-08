from django import forms


class TitleForm(forms.Form):
	title = forms.CharField(max_length=30)
	url = forms.URLField()


class AuthenticateForm(forms.Form):
	box = forms.ChoiceField(widget=forms.CheckboxInput, required=False)
	username = forms.CharField(max_length=30, required=False)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput, required=False)

