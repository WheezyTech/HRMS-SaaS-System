from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from attendance.models import Attendance
from employees.forms import EmployeeProfileForm
from payroll.models import Payroll
from .models import Employee
from django.db.models.signals import post_save
from django.dispatch import receiver


@login_required
def employee_dashboard(request):

    employee = getattr(request.user, "employee", None)

    if not employee:
        return render(request, "employees/no_profile.html")

    payrolls = Payroll.objects.filter(employee=employee).order_by("-id")
    attendance = Attendance.objects.filter(employee=employee).order_by("-id")

    return render(request, "employees/dashboard.html", {
        "employee": employee,
        "payrolls": payrolls,
        "attendance": attendance
    })

@login_required
def profile_update(request):

    employee, created = Employee.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = EmployeeProfileForm(request.POST, request.FILES, instance=employee)

        if form.is_valid():
            form.save()
            return redirect("employee_dashboard")

    else:
        form = EmployeeProfileForm(instance=employee)

    return render(request, "employees/profile_update.html", {
        "form": form,
        "employee": employee
    })

@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    if created and instance.role == 'employee':
        Employee.objects.create(user=instance)

def employee_dashboard(request):
    return render(request, "employees/dashboard.html")