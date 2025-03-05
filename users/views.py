from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import authenticate, login,logout



def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Basic validation
        if not all([first_name, last_name, email, password, password2]):
            messages.error(request, 'Please fill in all fields.')
            return redirect('register')

        if password != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken!')
            return redirect('register')

        user = CustomUser.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()

        # Auto-login after successful registration
        login(request, user)

        messages.success(request, 'Account created successfully! You can now log in.')
        return redirect('login')

    return render(request, 'users/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            if remember_me:
                request.session.set_expiry(1209600)
            else:
                request.session.set_expiry(0)  

            messages.success(request, 'Logged in successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')
    

def profile(request):
    return render(request, 'users/profile.html')
