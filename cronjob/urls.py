from django.urls import path
from .views import cronjobview, cronloginview, cronhomeview, cronregisterview, cronlogoutview


app_name = 'cronjob'
urlpatterns = [
    path('', cronhomeview.home, name='home'),
    path('logout/', cronlogoutview.userLogout, name='userLogout'),
    path('create/', cronjobview.createCronJob, name='createCronJob'),
    path('login/', cronloginview.userLogin, name='userLogin'),
    path('register/', cronregisterview.register, name='register'),
]
