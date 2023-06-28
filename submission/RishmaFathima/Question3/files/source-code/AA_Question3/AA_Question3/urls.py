"""
URL configuration for AA_Question3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_management.views import register, login


urlpatterns = [
   path('register/', register, name='register'),
   path('login/', user_login, name='login'),
   path('dashboard/', redirect_dashboard, name='dashboard'),
   path('customer_dashboard/', customer_dashboard, name='customer_dashboard'),
   path('technical_worker_dashboard/', technical_worker_dashboard, name='technical_worker_dashboard'),
   path('senior_management_dashboard/', senior_management_dashboard, name='senior_management_dashboard'),
   path('logout/', user_logout, name='logout'),
]






