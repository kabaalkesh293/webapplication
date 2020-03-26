from django.shortcuts import render, redirect
from crudapplication.forms import SalaryForm
from crudapplication.models.models import Employee
from crudapplication.models.salary import Salary


def addsalary(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
    else:
        form = SalaryForm()
    context = {'form': form, 'employees': employees}
    return render(request, 'add_salary.html', context)


