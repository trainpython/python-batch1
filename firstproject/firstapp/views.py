from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display_message(request):
    #return "Hello, Good Morning"
    return HttpResponse("Hello, Good Morning Welcome to Django")


def good_morning_view(request):
     #return "Hello, Good Morning"
     return HttpResponse("Hello Friends, Good Morning!!!")


def good_afternoon_view(request):
    #return "Hello, Good Morning"
    return HttpResponse("Hello Friends, Good Afternoon!!!")
