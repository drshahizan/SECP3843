

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Common fields for all user types
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    is_customer = models.BooleanField(default=False) 
    is_technical_worker = models.BooleanField(default=False)
    is_senior_management = models.BooleanField(default=False)
    
    senior_mgmt_field_1 = models.CharField(max_length=150)
    senior_mgmt_field_2 = models.CharField(max_length=150)

    def __str__(self):
        return self.username



