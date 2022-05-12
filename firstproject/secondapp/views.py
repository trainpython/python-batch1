from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def time_view(request):
    time = datetime.datetime.now()
    print(time)
    s="Hello Guys, Current Date and Time is "+str(time)
    return HttpResponse(s)

