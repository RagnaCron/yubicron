from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from cronjob.views.cronloginview import userLogin


# class CalculateScheduleTest(TestCase):
# 	pass
# def test_caluculate_schedule(self):
# 	minutes = MinutesForm(data={''})
# 	hours = HoursFrom(None)
# 	days = DaysFrom(None)
# 	user_defined = UserDefinedTimeForm(data='* * * * *')
# 	execution_time = calcSchedule(request, minutes, hours, days, user_defined)


class TestLoginView(TestCase):
	def setUp(self):
		self.credentials = {
			'username': 'testuser',
			'password': 'secret'}
		self.credentials2 = {
			'username': 'testmuser',
			'email': 'manuel.werder@csbe.ch',
			'password1': 'secret',
			'password2': 'secret',
		}
		User.objects.create(**self.credentials)

	def test_userLogin(self):
		response = self.client.get(reverse('cronjob:userLogin'))
		self.assertEqual(response.status_code, 200)
		response = self.client.post(reverse('cronjob:userLogin'), **self.credentials)
		self.assertTrue(response.status_code, 200)

	def test_userLogout(self):
		response = self.client.get(reverse('cronjob:userLogin'))
		self.assertEqual(response.status_code, 200)
		response = self.client.post(reverse('cronjob:userLogin'), **self.credentials)
		self.assertTrue(response.status_code, 200)
		response = self.client.post(reverse('cronjob:userLogout'))
		self.assertTrue(response.status_code, 200)

	def test_homeView(self):
		response = self.client.get(reverse('cronjob:home'))
		self.assertEqual(response.status_code, 200)


