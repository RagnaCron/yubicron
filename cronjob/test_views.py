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
		User.objects.create(username='Osiris', password='kloxet82', email='manuel.werder@csbe.ch')

	def test_userLogin(self):
		client = Client()
		response = client.get(reverse('cronjob:userLogin'))
		self.assertEqual(response.status_code, 200)


