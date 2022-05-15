from django.shortcuts import render
import datetime
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from templateApp.models import Employee
from templateApp.serializers import EmployeeSerilizer
from rest_framework.decorators import api_view


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


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    # find tutorial by pk (id)
    try:
        employee = Employee.objects.get(pk=pk)
        if request.method == 'GET':
            employee_serializer = EmployeeSerilizer(employee)
            return JsonResponse(employee_serializer.data)
        elif request.method == 'PUT':
            employee_data = JSONParser().parse(request)
            employee_serializer = EmployeeSerilizer(employee, data=employee_data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return JsonResponse(employee_serializer.data)
            return JsonResponse(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Employee.DoesNotExist:
        return JsonResponse({'message': 'The employee does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'DELETE'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            employees = employees.filter(title__icontains=title)
        tutorials_serializer = EmployeeSerilizer(employees, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = EmployeeSerilizer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 'safe=False' for objects serialization
#jinja tags