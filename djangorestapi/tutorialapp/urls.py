from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from tutorialapp import views

urlpatterns = [
    url(r'^api/employees$', views.employee_list),
    #url(r'^api/employee_detail/(?P<pk>[0-9]+)$', views.employee_detail),
]