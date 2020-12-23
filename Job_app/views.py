<<<<<<< HEAD
from django.shortcuts import render

def booking(request):
    return render(request,'booking.html')
    
def partner(request):
    return render(request,'partners.html')
=======
from django.shortcuts import render, redirect
from . import models
>>>>>>> b99e7a3388ad5f6dc4404a631cc28c9e5c0674be
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
