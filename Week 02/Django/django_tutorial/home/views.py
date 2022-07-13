from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Departments


def index(request):
    return render(request, 'index.html') 

def about(request):
    return render(request, 'about.html')

def bookings(request):
    return render(request, 'bookings.html')

def doctors(request):
    return render(request, 'doctors.html')

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dic_dept={
        'dept':Departments.objects.all()
    }
    return render(request, 'department.html', dic_dept)

