from django.core.mail import send_mail

def send_notification(email, subject, message):
    send_mail(
        subject,
        message,
        "hrms@company.com",
        [email],
        fail_silently=False,
    )

def get_redirect_url(user):
    if user.role == "admin":
        return "/dashboard/"
    elif user.role == "hr":
        return "/recruitment/dashboard/"
    elif user.role == "employee":
        return "/employees/dashboard/"
    return "/login/"