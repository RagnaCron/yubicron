from django import forms


class Authenticate(forms.Form):
	display = forms.ChoiceField(widget=forms.CheckboxInput,
	                            choices='authenticate',
	                            required=False)
