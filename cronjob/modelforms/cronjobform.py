from django.forms import ModelForm
from cronjob.models import CronJob


class CronJobForm(ModelForm):
	class Meta:
		model = CronJob
		fields = [
			'title',
			'url',
			'needsAuthentication',
			'userName',
			'password',
			'failMessage',
			'successMessage',
			'automaticJobStopperWhenToManyFailures',
			'willSaveMessage',
		]
