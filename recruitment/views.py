from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application
from .services import score_cv
from django.contrib.auth.decorators import login_required


# 📌 JOB LIST
def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request, "recruitment/job_list.html", {"jobs": jobs})


# 📌 JOB DETAIL
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    return render(request, "recruitment/job_detail.html", {
        "job": job
    })


# 📌 APPLY JOB (FIXED)
@login_required
def apply_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':

        app = Application.objects.create(
            job=job,

            full_name=request.POST.get("full_name", ""),
            email=request.POST.get("email", ""),
            phone=request.POST.get("phone", ""),
            gender=request.POST.get("gender", ""),
            date_of_birth=request.POST.get("date_of_birth", ""),
            location=request.POST.get("location", ""),

            institution=request.POST.get("institution", ""),
            qualification=request.POST.get("qualification", ""),
            graduation_year=request.POST.get("graduation_year", ""),

            current_position=request.POST.get("current_position", ""),
            experience=request.POST.get("experience", ""),

            certifications=request.POST.get("certifications", ""),
            memberships=request.POST.get("memberships", ""),

            referee_name=request.POST.get("referee_name", ""),
            referee_phone=request.POST.get("referee_phone", ""),
            referee_email=request.POST.get("referee_email", ""),

            cover_letter=request.POST.get("cover_letter", ""),

            cv=request.FILES.get("cv"),
        )
        app.ai_score = score_cv(app, job)
        app.save()

        return redirect('/recruitment/')

    return render(request, 'recruitment/apply.html', {
        'job': job
    })

# 📌 HR DASHBOARD
def recruitment_dashboard(request):
    return render(request, "recruitment/dashboard.html", {
        "applications": Application.objects.all().order_by("-id")[:10],
        "total_applications": Application.objects.count(),
        "active_jobs": Job.objects.filter(is_active=True).count(),
        "interviews": Application.objects.filter(status="interview").count(),
    })


# 📌 CREATE JOB
def create_job(request):

    if request.method == "POST":

        Job.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            requirements=request.POST["requirements"],
            location=request.POST["location"],
            is_active=request.POST.get("is_active") == "on"
        )

        return redirect("/recruitment/")

    return render(request, "recruitment/job_create.html")
