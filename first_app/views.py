from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return render(response, "first_app/base.html", {})


def home(response):
    return render(response, "first_app/home.html", {})
