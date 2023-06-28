# decorators.py
from django.contrib.auth.decorators import user_passes_test

def is_customer(user):
    return user.is_authenticated and user.is_customer

def is_technical_worker(user):
    return user.is_authenticated and user.is_technical_worker

def is_senior_management(user):
    return user.is_authenticated and user.is_senior_management
