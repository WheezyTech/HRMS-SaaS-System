from django.db import models
from employees.models import Employee

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)

    basic_salary = models.DecimalField(max_digits=12, decimal_places=2)
    gross_salary = models.DecimalField(max_digits=12, decimal_places=2)

    paye = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    nssf = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    sha = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    deductions = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)