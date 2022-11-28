from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_home, name='view_home'),
    path("jobs/", views.view_all_jobs, name='view_all_jobs'),
]