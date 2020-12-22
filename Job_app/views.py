from django.shortcuts import render, redirect
from . import models
# Create your views here.

def registration(request):
    return render(request,"registration.html")

def profile(request):
    return render(request,"profile.html")

