from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from attendance.forms import LeaveRequestForm
from .services import clock_in, clock_out

def clock_in_view(request):
    employee = request.user.employee
    clock_in(employee)
    return redirect("attendance_page")


def clock_out_view(request):
    employee = request.user.employee
    clock_out(employee)
    return redirect("attendance_page")

@login_required
def apply_leave(request):

    if request.method == "POST":
        form = LeaveRequestForm(request.POST)

        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = request.user
            leave.save()

            return redirect("employee_dashboard")

    else:
        form = LeaveRequestForm()

    return render(request, "attendance/apply_leave.html", {
        "form": form
    })