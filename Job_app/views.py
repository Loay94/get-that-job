from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
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

# to check if the email& user is in the database
def log_in(request):
    if request.method =='POST':
        user=models.log_in(request.POST)
        if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                    return redirect('/in')
    return redirect('/log_in')
#add booking page
def booking(request):
    return HttpResponse('go to booking page')
# add profile page
def profile(request):
    return HttpResponse('go to profile page')



