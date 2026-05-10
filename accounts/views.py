from django.shortcuts import render, redirect

from accounts.forms import CandidateRegisterForm
from accounts.utils import get_redirect_url

from .decorators import allowed_roles
from django.contrib.auth import login, authenticate

def candidate_register(request):

    form = CandidateRegisterForm()

    if request.method == 'POST':

        form = CandidateRegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.role = 'candidate'
            user.username = user.email
            user.save()

            return redirect('/login/')

    return render(request, 'accounts/register.html', {
        'form': form
    })

def login_success(request):
    return redirect(get_redirect_url(request.user))

@allowed_roles(['admin', 'hr'])
def hr_dashboard(request):
    return render(request, "dashboard/hr.html")

@allowed_roles(['employee'])
def employee_dashboard(request):
    return render(request, "employee/dashboard.html")