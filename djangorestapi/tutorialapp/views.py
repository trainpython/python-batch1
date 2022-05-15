from django.shortcuts import render
from rest_framework.decorators import api_view
from tutorialapp.models import Employee
from tutorialapp.serializers import EmployeeSerializer


# GET -->  Just to read the content (Ex: get employees and get employee by id)
# POST --> to create object (Ex: create/insert a new employee in table)
# PUT  --> to update object (Ex: to update employee info)
# DELETE --> to delete object (Ex: to delete employee(s))
from django.http.response import JsonResponse

# Create your views here.
@api_view(['GET','POST','DELETE'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)

