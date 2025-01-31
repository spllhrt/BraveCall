from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import User

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        dob = request.POST['dob']
        
        hashed_password = make_password(password)

        user = User(email=email, name=name, password=hashed_password, dob=dob)
        user.save()

        messages.success(request, "User registered successfully!")
        return redirect('login')
    return render(request, 'signup.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email)

            if check_password(password, user.password):
                messages.success(request, "Login successful!")
                return redirect('home')  
            else:
                messages.error(request, "Invalid password")
        except User.DoesNotExist:
            messages.error(request, "User not found")
    
    return render(request, 'login.html')

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def navbar(request):
    return render(request, 'admin/navbar.html')