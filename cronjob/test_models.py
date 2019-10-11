from django.contrib.auth.models import User
from django.test import TestCase
from .models import CronJob


# Create your tests here.
class CronJobTest(TestCase):
	def setUp(self):
		CronJob.objects.create(
			user=User.objects.create(username='Osiris', password='kloxet82', email='manuel.werder@csbe.ch'),
			title='Title Test',
			url='http://www.hello.com/',
			needs_authentication=False,
			username='',
			password='',
			execution_time='* * * * *',
			fail_message=False,
			success_message=False,
			automatic_job_stopper_when_to_many_failures=False,
			will_save_message=False
		)

	def test_CronJob_Model(self):
		cron = CronJob.objects.get(user=User.objects.get(username='Osiris'))
		user = User.objects.get(username='Osiris')
		self.assertEqual(cron.user, user)
		self.assertEqual(cron.title, 'Title Test')
		self.assertEqual(cron.url, 'http://www.hello.com/')
		self.assertEqual(cron.username, '')
		self.assertEqual(cron.password, '')
		self.assertEqual(cron.execution_time, '* * * * *')
		self.assertFalse(cron.fail_message)
		self.assertFalse(cron.success_message)
		self.assertFalse(cron.automatic_job_stopper_when_to_many_failures)
		self.assertFalse(cron.will_save_message)
