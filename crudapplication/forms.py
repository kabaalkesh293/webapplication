from django import forms
from crudapplication.models import Employee, Salary


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = "__all__"
