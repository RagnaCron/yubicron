from django import forms


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(label='Enter email', label_suffix='')
