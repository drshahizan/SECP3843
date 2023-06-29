# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.dashboard, name='home'),

    path('customer_dashboard', views.dashboard, name='customer_dashboard'),
    path('technical_worker_dashboard', views.dashboard, name='technical_dashboard'),
    path('management_dashboard', views.dashboard, name='management_dashboard'),

]
