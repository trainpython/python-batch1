from django.contrib import admin
from django.urls import path
from firstapp import views


urlpatterns = [
    path('displaymessage/', views.display_message),
    path('goodmorning/', views.good_morning_view),
    path('goodafternoon/', views.good_afternoon_view),
]