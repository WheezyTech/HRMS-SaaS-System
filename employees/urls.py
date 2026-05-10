from django.urls import path
from .views import employee_dashboard, profile_update

urlpatterns = [
    path("dashboard/", employee_dashboard, name="employee_dashboard"),
    path("profile/update/", profile_update, name="profile_update"),
]