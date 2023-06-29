from django.urls import path
from . import views
from .views import index, CustomerSignUpView, TechnicalSignUpView, SeniorSignUpView, cust_index, tech_index, senior_index

urlpatterns = [
    path('', index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('customer', CustomerSignUpView.as_view(), name='customer_signup'),
    path('senior', SeniorSignUpView.as_view(), name='senior_signup'),
    path('technical', TechnicalSignUpView.as_view(), name='technical_signup'),
    path('cust_index', cust_index, name='cust_index'),
    path('tech_index', tech_index, name='tech_index'),
    path('senior_index', senior_index, name='senior_index'),
]
