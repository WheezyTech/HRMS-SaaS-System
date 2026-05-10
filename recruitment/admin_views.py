from django.shortcuts import render
from .models import Application

def applications_dashboard(request):
    applications = Application.objects.all().order_by("-applied_at")

    return render(request, "recruitment/dashboard.html", {
        "applications": applications
    })