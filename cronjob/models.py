from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CronJob(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	title = models.CharField(max_length=50)
	url = models.URLField()

	needs_authentication = models.BooleanField()
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=30)

	execution_time = models.CharField(max_length=30)

	fail_message = models.BooleanField()
	success_message = models.BooleanField()
	automatic_job_stopper_when_to_many_failures = models.BooleanField()

	will_save_message = models.BooleanField()

	def __str__(self):
		return 'Cron Job - Username: {0}, Cron job title: {1}, Cron Job Time: {2}'\
			.format(self.user.username, self.title, self.execution_time)
