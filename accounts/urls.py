from django.urls import path
from .views import candidate_register

urlpatterns = [
    path('register/', candidate_register, name='candidate_register'),
]