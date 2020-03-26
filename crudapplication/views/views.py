from django.shortcuts import render, redirect
from crudapplication.forms import EmployeeForm, SalaryForm
from crudapplication.models.models import Employee


def create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(show)
            except:
                pass
    else:
        form = EmployeeForm()
    context = {'form': form}
    return render(request, 'create.html', context)


def show(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'show.html', context)


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect(show)


def edit(request, id):
    employee = Employee.objects.get(id=id)
    context = {'employee': employee}
    return render(request, 'edit.html', context)


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect(show)
    else:
        pass




