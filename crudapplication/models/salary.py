from django.db import models
from .models import Employee


class Salary(models.Model):
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    class Meta:
        db_table = 'salary'