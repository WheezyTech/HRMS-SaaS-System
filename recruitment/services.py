def score_cv(application, job):
    score = 0

    job_keywords = job.requirements.lower().split()
    cv_text = (application.cover_letter or "").lower()

    for word in job_keywords:
        if word in cv_text:
            score += 5

    if "python" in cv_text:
        score += 10

    if "degree" in cv_text:
        score += 5

    return min(score, 100)