# views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .decorators import is_customer, is_technical_worker, is_senior_management
from django.contrib.auth.decorators import user_passes_test




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print('User:', user) 
            if user is not None:
                login(request, user)
                print('User logged in successfully') 
                return redirect('dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    
    return render(request, 'profile.html', {'user': user})

@user_passes_test(is_customer)
def customer_dashboard(request):
    
    return render(request, 'customer_dashboard.html')

@user_passes_test(is_technical_worker)
def technical_worker_dashboard(request):
    
    return render(request, 'technical_worker_dashboard.html')

@user_passes_test(is_senior_management)
def senior_management_dashboard(request):
    
    return render(request, 'senior_management_dashboard.html')

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