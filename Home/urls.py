from django.contrib import admin
from django.urls import path, include
from Home import views


urlpatterns = [
    path('', views.Home, name='Home'),
    path('tasks', views.tasks, name='tasks')

]