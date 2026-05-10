from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

from accounts.views import hr_dashboard, login_success


urlpatterns = [
    path('admin/', admin.site.urls),

    # 🌍 APPS
    path('recruitment/', include('recruitment.urls')),
    path('employees/', include('employees.urls')),
    path('attendance/', include('attendance.urls')),
    path('payroll/', include('payroll.urls')),
    path('accounts/', include('accounts.urls')),

    path('', lambda request: redirect('/dashboard/')),

    # 📊 DASHBOARD
    path('dashboard/', hr_dashboard, name='hr_dashboard'),

    # 🔐 AUTH SYSTEM
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('login-success/', login_success, name='login_success'),
]

# 📁 MEDIA FILES
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )