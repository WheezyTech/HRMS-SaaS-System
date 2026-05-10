from django.db import models

# Create your models here.
from django.db import models
from employees.models import Employee

class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rating = models.IntegerField()  # 1–10 scale
    goals = models.TextField()
    feedback = models.TextField()
    review_date = models.DateField(auto_now_add=True)