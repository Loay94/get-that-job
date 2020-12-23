from django.urls import path
from . import views

urlpatterns = [
    path('/partner',views.partner),
    path('/booking',views.booking),
]