from django.shortcuts import render, redirect, HttpResponse

def home(request):
    return render(request, "home_page.html")