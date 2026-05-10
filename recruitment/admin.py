from django.contrib import admin
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "is_active", "created_at")
    search_fields = ("title", "location")

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'job', 'status', 'ai_score', 'applied_at']
    list_filter = ("status",)