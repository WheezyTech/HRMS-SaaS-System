from django.urls import path
from .views import dashboard_metrics_api, hr_dashboard, recruitment_dashboard

urlpatterns = [
    path("dashboard/", hr_dashboard, name="hr_dashboard"),
    path("metrics/", dashboard_metrics_api, name="dashboard_metrics"),
]