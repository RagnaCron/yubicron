from django import forms


class TitleForm(forms.Form):
	title = forms.CharField(max_length=30, label_suffix=' ', initial='Title...')
	url = forms.URLField(label_suffix=' ', initial='http://')


class AuthenticateForm(forms.Form):
	box = forms.BooleanField(widget=forms.CheckboxInput, required=False)
	username = forms.CharField(max_length=30, required=False,
	                           label_suffix=' ', label='Username')
	password = forms.CharField(max_length=20, widget=forms.PasswordInput,
	                           required=False, label='Password',
	                           label_suffix=' ')


MINUTES = [(0, 0), (1, 1)]


class MinutesForm(forms.Form):
	times = forms.ChoiceField(widget=forms.RadioSelect, choices=(0, 'Every'), required=True)
	# minutes = forms.ChoiceField(choices=MINUTES)


class UserMessageForm(forms.Form):
	failedJob = forms.BooleanField(widget=forms.CheckboxInput, required=False, label_suffix=' ')
	successfulJob = forms.BooleanField(widget=forms.CheckboxInput, required=False, label_suffix=' ')
	stopJob = forms.BooleanField(widget=forms.CheckboxInput, required=False)


class GeneralForm(forms.Form):
	willSaveMessage = forms.BooleanField(widget=forms.CheckboxInput, required=False, label_suffix=' ')
