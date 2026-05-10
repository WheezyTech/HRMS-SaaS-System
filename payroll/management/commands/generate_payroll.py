from django.core.management.base import BaseCommand
from employees.models import Employee
from payroll.services import generate_payroll

class Command(BaseCommand):
    help = "Generate payroll for all employees"

    def add_arguments(self, parser):
        parser.add_argument('--month', type=str, default="May 2026")

    def handle(self, *args, **options):

        month = options['month']
        employees = Employee.objects.all()

        if not employees:
            self.stdout.write(self.style.WARNING("No employees found"))
            return

        for emp in employees:
            generate_payroll(emp, month)

        self.stdout.write(self.style.SUCCESS(
            f"Payroll generated successfully for {employees.count()} employees"
        ))