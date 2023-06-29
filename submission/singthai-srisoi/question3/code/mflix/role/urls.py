from django.urls import path
from . import views
from .views import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('admin/', admin, name='admin'),
    path('senior/', views.senior, name='senior'),
    path('technical/', views.technical, name='technical'),
    path('customer/', views.customer, name='customer'),
    path('logout/', views.logout_view, name='logout_view'),
]