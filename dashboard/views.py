from django.shortcuts import render
from employees.models import Employee
from payroll.models import Payroll
from attendance.models import Attendance
from recruitment.models import Application
from django.db.models import Sum
from django.http import JsonResponse


def hr_dashboard(request):

    # 👤 Employee KPI
    total_employees = Employee.objects.count()

    # 📄 Applications KPI
    total_applications = Application.objects.count()

    # 🎤 Interviews KPI
    total_interviews = Application.objects.filter(
        status="interview"
    ).count()

    # 💰 Payroll KPI
    total_payroll = Payroll.objects.aggregate(
        total=Sum("net_salary")
    )["total"] or 0

    # ⏱ Attendance KPI
    total_attendance = Attendance.objects.count()

    context = {
        "total_employees": total_employees,
        "total_applications": total_applications,
        "total_interviews": total_interviews,
        "total_payroll": total_payroll,
        "total_attendance": total_attendance,
    }

    return render(request, "dashboard/hr_dashboard.html", context)

def dashboard_metrics_api(request):

    data = {
        "employees": Employee.objects.count(),
        "applications": Application.objects.count(),
        "attendance": Attendance.objects.count(),
        "payroll": Payroll.objects.aggregate(
            total=Sum("net_salary")
        )["total"] or 0,
    }

    return JsonResponse(data)