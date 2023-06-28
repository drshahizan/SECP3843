from django.urls import path
from django.urls import re_path
from .views import index,customer, technical_worker, senior_management


urlpatterns = [
    path('', index, name='index'),
    path('customer/', customer, name='customer'),
    path('technical_worker/', technical_worker, name='technical_worker'),
    path('senior_management/', senior_management, name='senior_management'),
]