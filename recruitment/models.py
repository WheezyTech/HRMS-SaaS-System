from django.db import models
from django.conf import settings


class Job(models.Model):
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    description = models.TextField()
    requirements = models.TextField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):

    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('reviewing', 'Reviewing'),
        ('interview', 'Interview'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    # PERSONAL INFO
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    # EDUCATION
    institution = models.CharField(max_length=255, blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    graduation_year = models.CharField(max_length=10, blank=True, null=True)

    # EXPERIENCE
    current_position = models.CharField(max_length=255, blank=True, null=True)
    experience = models.TextField(blank=True, null=True)

    # PROFESSIONAL
    certifications = models.TextField(blank=True, null=True)
    memberships = models.TextField(blank=True, null=True)

    # REFEREES
    referee_name = models.CharField(max_length=255, blank=True, null=True)
    referee_phone = models.CharField(max_length=20, blank=True, null=True)
    referee_email = models.EmailField(blank=True, null=True)

    # APPLICATION FILES
    cv = models.FileField(upload_to="cvs/")
    cover_letter = models.TextField(blank=True, null=True)

    # AI SCORE
    ai_score = models.IntegerField(default=0)

    # STATUS
    status = models.CharField(
        max_length=50,
        default="pending"
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name