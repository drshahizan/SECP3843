from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            # Form is not valid, display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            # You can also add a general error message if needed
            messages.error(request, 'Error during registration. Please fix the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


@login_required
def dashboard(request):
    user = request.user
    if user.is_customer:
        return render(request, 'customer_dashboard.html')
    elif user.is_technical_worker:
        return render(request, 'technical_worker_dashboard.html')
    elif user.is_senior_management:
        return render(request, 'senior_management_dashboard.html')
    else:
        return redirect('profile')


def redirect_dashboard(request):
    user = request.user
    if user.is_customer:
        return redirect('customer_dashboard')
    elif user.is_technical_worker:
        return redirect('technical_worker_dashboard')
    elif user.is_senior_management:
        return redirect('senior_management_dashboard')
    else:
        return redirect('profile')
    
def user_logout(request):
    logout(request)
    return redirect('login')
