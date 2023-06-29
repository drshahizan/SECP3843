from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .models import Customer,Senior, Technical,User
from django.views.generic import CreateView
from .forms import CustomerSignUpForm,SeniorSignUpForm,TechnicalSignUpForm
from django.contrib import auth

def login_view(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            if user.is_customer:
                return redirect('cust_index')
            elif user.is_technical:
                return redirect('tech_index')
            elif user.is_senior:
                return redirect('senior_index')
        else:
            return render (request,'user/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'user/login.html')
    
def index(request):
    return render(request,'index.html')

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        form.save()
        return redirect('cust_index')
    
class TechnicalSignUpView(CreateView):
    model = User
    form_class = TechnicalSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'technical'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        form.save()
        return redirect('tech_index')
    
class SeniorSignUpView(CreateView):
    model = User
    form_class = SeniorSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'senior'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        form.save()
        return redirect('senior_index')

def cust_index(request):
    return render(request, 'cust_index.html')

def tech_index(request):
    username = request.user.username
    return render(request, 'tech_index.html')

def senior_index(request):
    username = request.user.username
    return render(request, 'senior_index.html')

