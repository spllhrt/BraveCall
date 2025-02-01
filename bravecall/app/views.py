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

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('signup')

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
                request.session['user_id'] = user.id  
                request.session['user_name'] = user.name

                messages.success(request, "Login successful!")
                return redirect('profile')  
            else:
                messages.error(request, "Invalid password")
        except User.DoesNotExist:
            messages.error(request, "User not found")
    
    return render(request, 'login.html')


def logout_user(request):
    request.session.flush()
    messages.success(request, "You have been logged out!")
    return redirect('login')


def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def navbar(request):
    return render(request, 'admin/navbar.html')

def update_password(request):
    if 'user_id' not in request.session:  
        messages.error(request, "You must be logged in to update your password.")
        return redirect('login')  

    try:
        user = User.objects.get(id=request.session['user_id'])  # Fetch logged-in user
    except User.DoesNotExist:
        messages.error(request, "User not found!")
        return redirect('login')

    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        # Check if old password is correct
        if not check_password(old_password, user.password):
            messages.error(request, "Old password is incorrect!")
            return redirect("profile")

        # Check if new passwords match
        if new_password != confirm_password:
            messages.error(request, "New passwords do not match!")
            return redirect("profile")

        # Ensure new password is not empty
        if not new_password.strip():
            messages.error(request, "New password cannot be empty!")
            return redirect("profile")

        # Hash and save the new password
        user.password = make_password(new_password)
        user.save()

        messages.success(request, "Password updated successfully!")
        return redirect("profile")  

    return render(request, "user/profile.html", {"user": user})  