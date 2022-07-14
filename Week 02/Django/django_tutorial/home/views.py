from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
from .models import Departments
from .models import Doctors
from .forms import BookingForm


def index(request):
    return render(request, 'index.html') 

def about(request):
    return render(request, 'about.html')

def bookings(request):
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'bookings.html', dict_form)

def doctors(request):
    dic_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dic_docs)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dic_dept={
        'dept':Departments.objects.all()
    }
    return render(request, 'department.html', dic_dept)

