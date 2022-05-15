from django.db import models
#create table employee(eno int,ename varchar(30))
# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)
    ecomp = models.CharField(max_length=30,default='Infosys')
    #
    class Meta:
        db_table = 'Employee'

