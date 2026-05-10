from django.shortcuts import render, redirect
from .models import LeaveRequest

def leave_dashboard(request):

    leaves = LeaveRequest.objects.all().order_by("-created_at")

    return render(request, "attendance/leave_dashboard.html", {
        "leaves": leaves
    })


def approve_leave(request, leave_id):
    leave = LeaveRequest.objects.get(id=leave_id)
    leave.status = "approved"
    leave.save()
    return redirect("/attendance/leave-dashboard/")


def reject_leave(request, leave_id):
    leave = LeaveRequest.objects.get(id=leave_id)
    leave.status = "rejected"
    leave.save()
    return redirect("/attendance/leave-dashboard/")