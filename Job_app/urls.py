from django.urls import path
from . import views

urlpatterns = [
    path('',views.partner),
    path('/booking',views.booking),
]