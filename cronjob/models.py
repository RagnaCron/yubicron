from django.db import models

# Create your models here.


class CronJob(models.Model):
	user = models.ForeignKey(on_delete=models.CASCADE)

	title = models.CharField(max_length=50)
	url = models.URLField

	needs_authentication = models.BooleanField
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=30)

	execution_time = models.CharField(max_length=30)

	fail_message = models.BooleanField
	success_message = models.BooleanField
	automatic_job_stopper_when_to_many_failures = models.BooleanField

	will_save_message = models.BooleanField
