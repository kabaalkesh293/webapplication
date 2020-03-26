from django.db import models


class Employee(models.Model):
    empid = models.CharField(max_length=10)
    empname = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=15)

    class Meta:
        db_table = 'employees'

