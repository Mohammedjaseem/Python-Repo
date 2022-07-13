from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
num = {
    'num':[1,2,3,4,5,6,7,8,9]
}


def index(request):
    return render(request, 'index.html',num) 

def about(request):
    return render(request, 'about.html')

def bookings(request):
    return render(request, 'bookings.html')

def doctors(request):
    return render(request, 'doctors.html')

def contact(request):
    return render(request, 'contact.html')

def department(request):
    return render(request, 'department.html')

