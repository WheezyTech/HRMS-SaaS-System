from decimal import Decimal

def calculate_payroll(basic_salary, allowances=0):

    basic_salary = Decimal(basic_salary)
    allowances = Decimal(allowances)

    PAYE_RATE = Decimal("0.30")
    NSSF_RATE = Decimal("0.06")
    SHA_RATE = Decimal("0.02")

    paye = basic_salary * PAYE_RATE
    nssf = basic_salary * NSSF_RATE
    sha = basic_salary * SHA_RATE

    total_deductions = paye + nssf + sha
    gross = basic_salary + allowances
    net_salary = gross - total_deductions

    return {
        "paye": paye,
        "nssf": nssf,
        "sha": sha,
        "deductions": total_deductions,
        "net_salary": net_salary
    }