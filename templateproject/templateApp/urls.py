from django.conf.urls import url
from templateApp import views

urlpatterns = [
    url(r'^api/employees$', views.employee_list),
    url(r'^api/employee_detail/(?P<pk>[0-9]+)$', views.employee_detail),
]