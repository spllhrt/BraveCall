from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

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

def dashboard(request):
    if 'user_id' not in request.session:
        messages.error(request, "You must be logged in to access this page.")
        return redirect('login')

    try:
        user = User.objects.get(id=request.session['user_id'])
    except User.DoesNotExist:
        messages.error(request, "User not found!")
        return redirect('login')
    
    return render(request, 'admin/dashboard.html')


def update_profile(request):
    if 'user_id' not in request.session:  
        messages.error(request, "You must be logged in to update your profile.")
        return redirect('login')  

    try:
        user = User.objects.get(id=request.session['user_id'])
    except User.DoesNotExist:
        messages.error(request, "User not found!")
        return redirect('login')

    if request.method == "POST":
        if 'profile_picture' in request.FILES:
            profile_picture = request.FILES['profile_picture']

            profile_pics_dir = os.path.join(settings.MEDIA_ROOT, 'profile_pics')
            if not os.path.exists(profile_pics_dir):
                os.makedirs(profile_pics_dir)

            fs = FileSystemStorage(location=profile_pics_dir)
            filename = fs.save(profile_picture.name, profile_picture)
            file_url = fs.url("profile_pics/" + filename)

            if file_url.startswith('/media'):
                file_url = file_url[6:]

            user.profile_picture = file_url
            user.save()

            messages.success(request, "Profile picture updated successfully!")

        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if old_password and not check_password(old_password, user.password):
            messages.error(request, "Old password is incorrect!")
            return redirect("profile")

        if new_password and new_password != confirm_password:
            messages.error(request, "New passwords do not match!")
            return redirect("profile")

        if new_password and not new_password.strip():
            messages.error(request, "New password cannot be empty!")
            return redirect("profile")

        if new_password:
            user.password = make_password(new_password)
            user.save()

            messages.success(request, "Password updated successfully!")

        return redirect("profile")  

    return render(request, "user/profile.html", {"user": user})