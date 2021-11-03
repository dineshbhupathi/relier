from django.contrib import admin
from django.conf.urls import url
from .views import *
app_name = 'users'
urlpatterns = [
    url('users/', Users.as_view()),
]
