from django.shortcuts import render, redirect
from . import models
# Create your views here.

def registration(request):
    return render(request,"registration.html")

def profile(request):
    return render(request,"profile.html")

# to view the main page without sign in:
def home(request): 
    return render(request, "home_page.html")
# to view the main page after sign in :
def home_in(request):
    return render(request, "home_in.html")



