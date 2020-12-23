from django.shortcuts import render

def booking(request):
    return render(request,'booking.html')
    
def partner(request):
    return render(request,'partners.html')
# Create your views here.
