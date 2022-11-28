from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def view_home(response):
    return HttpResponse("<h1>Let's find you a job in Europe!</h1>")


def view_all_jobs(response):
    return HttpResponse("Here you will find all the jobs in Europe")



