from rest_framework import serializers
from tutorialapp.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
      class Meta:
          model=Employee
          fields=('eno','ename','esal','eaddr','ecomp')