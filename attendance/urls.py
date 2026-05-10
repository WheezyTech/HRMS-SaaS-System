from django.urls import path

from attendance.admin_views import approve_leave, reject_leave
from .views import apply_leave, clock_in_view, clock_out_view
from .admin_views import leave_dashboard, approve_leave, reject_leave

urlpatterns = [
    path("clock-in/", clock_in_view),
    path("clock-out/", clock_out_view),
    path("leave/apply/", apply_leave, name="apply_leave"),
    path("leave-dashboard/", leave_dashboard, name="leave_dashboard"),
    path("leave/<int:leave_id>/approve/", approve_leave),
    path("leave/<int:leave_id>/reject/", reject_leave),
]