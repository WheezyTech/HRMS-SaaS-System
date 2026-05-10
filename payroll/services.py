from .models import Payroll
from .utils import calculate_payroll

def generate_payroll(employee, month):

    result = calculate_payroll(employee.salary)

    payroll = Payroll.objects.create(
        employee=employee,
        month=month,
        basic_salary=employee.salary,
        paye=result["paye"],
        nssf=result["nssf"],
        sha=result["sha"],
        deductions=result["deductions"],
        net_salary=result["net_salary"]
    )

    return payroll