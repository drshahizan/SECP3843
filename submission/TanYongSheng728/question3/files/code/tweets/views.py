from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .form import UserRegistrationForm, LoginForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'This email have been registered!')
                    return redirect('signup')
                elif User.objects.filter(username=username).exists():
                    messages.warning(request, 'This username have been registered!')
                    return redirect('signup')
                else:
                    messages.success(request, 'Account successfully created!')
                    user = form.save(commit=False)
                    user.set_password(form.cleaned_data['password'])
                    user.save()
                    return redirect('signin')
            else:
                messages.warning(request, 'Password not matching!')
                return redirect('signup')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        form = LoginForm(request.POST)
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.user_type == 'customer':
                return redirect('customer')
            elif user.user_type == 'technical_worker':
                return redirect('technical_worker')
            elif user.user_type == 'senior_management':
                return redirect('management')
        else:
            messages.warning(request, 'Credentials Invalid. Please register first.')
            return redirect('signup')
        
    else:
        form = LoginForm()
    return render(request, 'signin.html', {'form': form})
    
def customer(request):
    return render(request, 'customer.html')

def technical_worker(request):
    return render(request, 'technical_worker.html')
    
def management(request):
    return render(request, 'management.html')