from django.urls import path
from .views import create_job, job_list, job_detail, apply_job, recruitment_dashboard
from .admin_views import applications_dashboard

urlpatterns = [
    path("", job_list, name="job_list"),  # 👈 THIS FIXES /recruitment/
    path("<int:job_id>/", job_detail, name="job_detail"),
    path("<int:job_id>/apply/", apply_job, name="apply_job"),

    # HR dashboard inside recruitment
    path("dashboard/applications/", applications_dashboard, name="applications_dashboard"),
    path("dashboard/create-job/", create_job, name="create_job"),
    path("dashboard/", recruitment_dashboard, name="recruitment_dashboard"),
    path("jobs/create/", create_job, name="create_job"),

]