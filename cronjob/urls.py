from django.urls import path
from .views import cronjobview, loginview, cronhomeview

app_name = 'cronjob'

urlpatterns = [
    path('', cronhomeview.home, name='home'),
    path('/create', cronjobview.createCronJob, name='createCronJob'),
    path('/login', loginview.userLogin, name='login'),
]
