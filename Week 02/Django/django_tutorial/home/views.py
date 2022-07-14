from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.
from .models import Departments
from .models import Doctors
from .forms import BookingForm
from .forms import NewUserForm



def index(request):
    return render(request, 'index.html') 

def about(request):
    return render(request, 'about.html')

def bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confrm.html')
    else:       
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

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)   
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f"New account created: {username}")
      login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    else:
      messages.error(request,"Account creation failed")

    return redirect("main:homepage")

  form = UserCreationForm()
  return render(request,"register.html", {"form": form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")

