from django.utils import timezone
from .models import Attendance

def clock_in(employee):

    today = timezone.now().date()

    attendance, created = Attendance.objects.get_or_create(
        employee=employee,
        date=today
    )

    if attendance.check_in:
        return "Already clocked in"

    attendance.check_in = timezone.now()
    attendance.save()

    return "Clock-in successful"


def clock_out(employee):

    today = timezone.now().date()

    try:
        attendance = Attendance.objects.get(employee=employee, date=today)
    except Attendance.DoesNotExist:
        return "No clock-in found"

    if not attendance.check_in:
        return "You must clock in first"

    if attendance.check_out:
        return "Already clocked out"

    attendance.check_out = timezone.now()
    attendance.save()

    return "Clock-out successful"