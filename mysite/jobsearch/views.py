from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def base(response):
    return render(response, "jobsearch/base.html", {})


def home(response):
    return render(response, "jobsearch/home.html", {})


def filter_jobs_form(response):
    return render(response, "jobsearch/filter_jobs_form.html", {})


def search_results(response):
    return render(response, "jobsearch/search_results.html", {})
