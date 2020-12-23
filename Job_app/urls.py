from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('in',views.home_in),
     path('register', views.registration),
    path('profile',views.profile),
    path('partner',views.partner),
    path('booking',views.booking),

]