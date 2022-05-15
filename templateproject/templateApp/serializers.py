from rest_framework import serializers
from templateApp.models import Employee

class EmployeeSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('eno','ename','esal','eaddr')

