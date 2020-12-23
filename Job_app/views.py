from django.shortcuts import render, redirect, HttpResponse

# to view the main page without sign in:
def home(request): 
    return render(request, "home_page.html")
# to view the main page after sign in :
def home_in(request):
    return render(request, "home_in.html")
# 