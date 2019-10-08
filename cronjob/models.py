from django.db import models

# Create your models here.


class CronJob(models.Model):
	title = models.CharField(max_length=50)
	url = models.URLField

	needsAuthentication = models.BooleanField
	userName = models.CharField(max_length=20)
	password = models.CharField(max_length=30)

	executionTime = models.CharField(max_length=30)

	hasMailMessages = models.BooleanField
	failMessage = models.TextField
	successMessage = models.TextField
	automaticJobStopperWhenToManyFailure = models.BooleanField

	willSaveMessage = models.BooleanField
	savedMessage = models.TextField

