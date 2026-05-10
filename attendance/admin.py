from django.contrib import admin
from .models import LeaveRequest

@admin.register(LeaveRequest)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ("employee", "status", "start_date", "end_date", "created_at")
    list_filter = ("status",)