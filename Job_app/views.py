
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . import models


#to render the registration page
def registration_page(request):
    return render(request,"registration.html")

#to process the user info from registration form (checks for validation) and redirects to Home_in page
def registration(request):
    if request.method == 'POST':
        errors = models.User.objects.register_validator(request.POST) 
        if len(errors) > 0:  
            for key, value in errors.items():
                messages.error(request, value) #show the messages value
            return redirect('/register-page')                                                                   
        else: #if there are no errors >> create new user
            user = models.add_new_user(request.POST)
            if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                return redirect('/in')
    return redirect('/register-page') 

#for login
def login(request):
    if request.method =='POST':
        errors = models.User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = models.user_login(request.POST)
            if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                return redirect('/quotes')
    return redirect('/')

#to view the user's profile 
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
# add profile page
def profile(request):
    return HttpResponse('go to profile page')

#adding 
def booking(request):
    return render(request,'booking.html')

#adding partners
def partner(request):
    return render(request,'partners.html')

