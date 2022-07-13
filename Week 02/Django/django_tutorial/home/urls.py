from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('bookings' , views.bookings, name='bookings'),
    path('doctors' , views.doctors, name='doctors'),
    path('contact' , views.contact, name='contact'),
    path('department' , views.department, name='departments'),
]