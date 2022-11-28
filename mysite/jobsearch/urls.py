from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("home", views.home, name="home"),
    path("filter_jobs_form", views.filter_jobs_form, name="filter_jobs_form"),
    path("search_results", views.search_results, name="search_results")
]
