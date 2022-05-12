from django.contrib import admin
from django.urls import path
from secondapp import views
#from firstproject.secondapp.views import time_view

urlpatterns = [
    path('getdatetime/', views.time_view),
]