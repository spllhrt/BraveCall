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
        
        # Hash the password before saving it
        hashed_password = make_password(password)

        # Create and save the user
        user = User(email=email, name=name, password=hashed_password, dob=dob)
        user.save()

        messages.success(request, "User registered successfully!")
        return redirect('login')  # Redirect to login page after successful signup
    return render(request, 'signup.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            # Find the user by email
            user = User.objects.get(email=email)

            # Check if the password matches
            if check_password(password, user.password):
                # Successful login (you can add a session or authentication logic here)
                messages.success(request, "Login successful!")
                return redirect('home')  # Redirect to a home page or dashboard
            else:
                messages.error(request, "Invalid password")
        except User.DoesNotExist:
            messages.error(request, "User not found")
    
    return render(request, 'login.html')

def homepage(request):
    # Homepage view logic here
    return render(request, 'homepage.html')

def about(request):
    # About page view logic here
    return render(request, 'about.html')