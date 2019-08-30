from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
       path('contact/', views.contact),
       path('contact/<str: link>/', views.contact_address),
]