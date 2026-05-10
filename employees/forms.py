from django import forms
from .models import Employee

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'phone',
            'department',
            'job_title',
            'address',
            'profile_picture'
        ]