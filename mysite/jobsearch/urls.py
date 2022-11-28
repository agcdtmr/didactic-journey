from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("", views.home, name="home"),
    path("", views.filter_jobs_form, name="filter_jobs_form")
]
