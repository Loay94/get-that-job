from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('in',views.home_in),
    path('register', views.registration),
    path('profile',views.profile),
    path('log_in',views.log_in),
    path('booking',views.booking),
    path('register-page', views.registration_page),
    path('partner',views.partner),
    
]