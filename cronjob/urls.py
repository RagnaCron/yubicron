from django.urls import path
from . import views

app_name = 'cronjob'
urlpatterns = [
    path('', views.index, name='index'),
]