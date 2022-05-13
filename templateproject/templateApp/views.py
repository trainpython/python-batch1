from django.shortcuts import render
import datetime
# Create your views here.
def wish_view(request):
    date = datetime.datetime.now()
    name='Kasi'
    rollno='1111'
    marks=100
    response_dict = {'current_date': date,'name':name,'rollno':rollno,'marks':marks}
    return render(request,'templateApp/wish.html',context=response_dict)


def wish_based_on_time_view(request):
    date = datetime.datetime.now()
    hour = int(date.strftime('%H'))
    wish_msg="Hello Friends!! "
    if(hour<12):
        wish_msg+="Good morning"
    elif(hour<16):
        wish_msg += "Good Afternoon"
    elif(hour<21):
        wish_msg += "Good Evening"
    else:
        wish_msg += "Good night"

    response_dict = {'current_date': date,'wish_msg':wish_msg}
    return render(request,'templateApp/wishontime.html',context=response_dict)

#jinja tags