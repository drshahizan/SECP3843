from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('customer/', views.customer, name='customer'),
    path('technical/', views.technical, name='technical'),
    path('senior/', views.senior, name='senior'),
]