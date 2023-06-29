from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def register_view(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            role = request.POST.get('role')
            
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                error_message = "Username already exists. Please choose a different username."
                return render(request, 'register.html', {'error_message': error_message})

    return render(request, 'register.html')

def index_view(request):
    # Add your logic here
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        # Retrieve the username and password from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'password':
            # If the login is successful, you can redirect to a success page
            return redirect('/success/')
        else:
            # If the login fails, you can render the login page again with an error message
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})

    # If the request method is GET, render the login page
    return render(request, 'login.html')