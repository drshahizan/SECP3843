from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserProfile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.urls import reverse_lazy

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            name = form.cleaned_data['name']

            user = CustomUser.objects.create_user(username=username, password=password)
            profile = UserProfile(user=user, user_type=user_type, name=name)
            profile.save()

            saved_user = UserProfile.objects.get(user=user)

            return render(request, 'registration_success.html', {'user': saved_user})
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('redirect_user')

    def get_success_url(self):
        return 'redirect_user'

def redirect_user(request):
    user_type = request.user.userprofile.user_type

    if user_type == 'customer':
        return redirect('customer_dashboard')  # Replace 'customer_dashboard' with the URL name of the customer dashboard view
    elif user_type == 'worker':
        return redirect('worker_dashboard')  # Replace 'worker_dashboard' with the URL name of the worker dashboard view
    elif user_type == 'management':
        return redirect('management_dashboard')  # Replace 'management_dashboard' with the URL name of the management dashboard view


def home(request):
    return render(request, 'index.html') 

@login_required
def customer_dashboard_view(request):
    return render(request, 'question3app/customer_dashboard_view.html')

@login_required
def worker_dashboard_view(request):
    return render(request, 'question3app/worker_dashboard_view.html')

@login_required
def management_dashboard_view(request):
    return render(request, 'question3app/management_dashboard_view.html')