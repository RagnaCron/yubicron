from django import forms


class TitleForm(forms.Form):
	title = forms.CharField(max_length=30, label_suffix=' ', initial='Title...')
	url = forms.URLField(label='Url  ', label_suffix=' ', initial='http://')


class AuthenticateForm(forms.Form):
	box = forms.BooleanField(required=False, label='Needs Authentication', label_suffix=' ')
	username = forms.CharField(max_length=30, required=False,
	                           label_suffix=' ', label='Username')
	password = forms.CharField(max_length=20, widget=forms.PasswordInput,
	                           required=False, label='Password',
	                           label_suffix=' ')


class MinutesForm(forms.Form):
	each_minute = forms.IntegerField(min_value=0, max_value=59, initial=0, label='Each', label_suffix=' ', required=False)


class HoursFrom(forms.Form):
	every_hour = forms.IntegerField(min_value=0, max_value=23, initial=0, label_suffix=' ', required=False)
	every_minute = forms.IntegerField(min_value=0, max_value=59, initial=0, label_suffix=' ', required=False)


class DaysFrom(forms.Form):
	every_month_day = forms.IntegerField(min_value=1, max_value=31, initial=1, label_suffix=' ', required=False)
	every_hours_day = forms.IntegerField(min_value=0, max_value=23, initial=0, label_suffix=' ', required=False)
	every_minute_day = forms.IntegerField(min_value=0, max_value=59, initial=0, label_suffix=' ', required=False)


class UserDefinedTimeForm(forms.Form):
	user_defined = forms.CharField(min_length=9, max_length=20, initial='* * * * *',
	                               label='User defined', label_suffix=' ')


class UserMessageForm(forms.Form):
	failed_job = forms.BooleanField(required=False, label_suffix=' ')
	successful_job = forms.BooleanField(required=False, label_suffix=' ')
	stop_job = forms.BooleanField(required=False)


class GeneralForm(forms.Form):
	will_save_message = forms.BooleanField(required=False, label_suffix=' ')
