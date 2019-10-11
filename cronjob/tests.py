from django.contrib.auth.models import User
from django.http import request
from django.test import TestCase

from cronjob.forms.cronjob.cronjobforms import HoursFrom, DaysFrom, UserDefinedTimeForm, MinutesForm, TitleForm, \
	AuthenticateForm, UserMessageForm, GeneralForm
from cronjob.views.cronjobview import calcSchedule
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


# class CalculateScheduleTest(TestCase):
# 	pass
	# def test_caluculate_schedule(self):
	# 	minutes = MinutesForm(data={''})
	# 	hours = HoursFrom(None)
	# 	days = DaysFrom(None)
	# 	user_defined = UserDefinedTimeForm(data='* * * * *')
	# 	execution_time = calcSchedule(request, minutes, hours, days, user_defined)


class CronJobFormsTest(TestCase):
	def test_title_form(self):
		title = TitleForm(data={'title': 'Test', 'url': 'http://www.hello.ch/'})
		title_false = TitleForm(data={'title': '', 'url': 'http://www.hello.ch/'})
		title_url_false = TitleForm(data={'title': 'Test', 'url': '...hehhel'})
		self.assertTrue(title.is_valid())
		self.assertFalse(title_false.is_valid())
		self.assertFalse(title_url_false.is_valid())

	def test_auth_form(self):
		authenticate = AuthenticateForm(data={'box': False, 'username': '', 'password': ''})
		self.assertTrue(authenticate.is_valid())

	def minutes_form(self):
		minutes_false = MinutesForm(data={'each_minute': 66})
		minutes = MinutesForm(data={'each_minute': 56})
		self.assertFalse(minutes_false.is_valid())
		self.assertTrue(minutes.is_valid())

	def test_hours_form(self):
		hour_false = HoursFrom(data={'every_hour': 24, 'every_minute': 33})
		hour = HoursFrom(data={'every_hour': 23, 'every_minute': 33})
		self.assertFalse(hour_false.is_valid())
		self.assertTrue(hour.is_valid())

	def test_day_form(self):
		days_false = DaysFrom(data={'every_hours_day': 24, 'every_month_day': 33, 'every_minute_day': 0})
		days = DaysFrom(data={'every_hours_day': 23, 'every_month_day': 31, 'every_minute_day': 44})
		self.assertFalse(days_false.is_valid())
		self.assertTrue(days.is_valid())

	# def test_user_defined_cron_job_form(self):
	# 	# SHOULD ASSERT FALSE
	# 	cron_job0 = UserDefinedTimeForm(data={'user_defined': '69 * * * 0-1'})
	# 	self.assertFalse(cron_job0.is_valid())
	# 	cron_job1 = UserDefinedTimeForm(data={'user_defined': '0-1 * * * 0'})
	# 	self.assertFalse(cron_job1.is_valid())
	# 	cron_job2 = UserDefinedTimeForm(data={'user_defined': '69 * * * 0'})
	# 	self.assertFalse(cron_job2.is_valid())
	#
	# 	# SHOULD ASSERT TRUE
	# 	cron_job3 = UserDefinedTimeForm(data={'user_defined': '* * * * *'})
	# 	self.assertTrue(cron_job3.is_valid())
	# 	cron_job4 = UserDefinedTimeForm(data={'user_defined': '0-4 * * * *'})
	# 	self.assertTrue(cron_job4.is_valid())
	# 	cron_job5 = UserDefinedTimeForm(data={'user_defined': '12-45 2,3-4 1-31 * 7'})
	# 	self.assertTrue(cron_job5.is_valid())
	# 	# cron_job6 = UserDefinedTimeForm(data={'user_defined': '*/45 2,3-4 */1-31 * 6'})
	# 	# self.assertTrue(cron_job6.is_valid())

	def test_user_message_from(self):
		message = UserMessageForm(data={'failed_job': None, 'successful_job': False, 'stop_job': False})
		message2 = UserMessageForm(data={'failed_job': True, 'successful_job': None, 'stop_job': None})

		self.assertFalse(message['failed_job'].value())
		self.assertFalse(message['stop_job'].value())
		self.assertFalse(message['successful_job'].value())

		self.assertTrue(message2['failed_job'].value())
		self.assertFalse(message2['successful_job'].value())
		self.assertFalse(message2['stop_job'].value())

	def test_general_form(self):
		message_none = GeneralForm(data={'will_save_message': None})
		message_false = GeneralForm(data={'will_save_message': False})
		message_true = GeneralForm(data={'will_save_message': True})

		self.assertFalse(message_none['will_save_message'].value())
		self.assertFalse(message_false['will_save_message'].value())
		self.assertTrue(message_true['will_save_message'].value())
