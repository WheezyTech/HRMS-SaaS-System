from django.shortcuts import render, redirect

from .models import Payroll
from django.shortcuts import get_object_or_404


def generate_payroll(employee):
    result = calculate_pay(employee.salary)

    Payroll.objects.create(
        employee=employee,
        month="May 2026",
        basic_salary=employee.salary,
        deductions=result["paye"] + result["nssf"] + result["sha"],
        net_salary=result["net_salary"]
    )

def payroll_dashboard(request):
    payrolls = Payroll.objects.all()
    return render(request, "payroll/dashboard.html", {"payrolls": payrolls})

def payslip_view(request, payroll_id):
    payroll = get_object_or_404(Payroll, id=payroll_id)

    return render(request, "payroll/payslip.html", {
        "payroll": payroll
    })

def payroll(request):

    if request.user.role not in ['admin', 'hr']:
        return redirect('dashboard')

    return render(request, 'payroll/index.html')