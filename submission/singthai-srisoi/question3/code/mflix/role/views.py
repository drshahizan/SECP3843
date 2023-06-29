from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created'
            return redirect('login_view')
        else:
            msg = 'Form is not valid'
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password =  form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_senior:
                login(request, user)
                return redirect('senior')
            elif user is not None and user.is_technical:
                login(request, user)
                return redirect('technical')
            elif user is not None and user.is_admin:
                login(request, user)
                return redirect('admin')
            else:
                msg = 'Form submission successful'
        else:
            msg = 'Form is not valid'
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'msg': msg})


def home(request):
    return render(request, 'home.html')

def customer(request):
    return render(request, 'customer.html')

def technical(request):
    return render(request, 'technical.html')

def senior(request):
    return render(request, 'senior.html')

def admin(request):
    return redirect('admin')

def logout_view(request):
    logout(request)
    return redirect('index')