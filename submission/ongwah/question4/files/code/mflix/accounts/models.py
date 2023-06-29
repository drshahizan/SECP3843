from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPES = [
        ('customer', 'Customer'),
        ('technical', 'Technical Worker'),
        ('management', 'Senior Management'),
    ]
    user_type = models.CharField(max_length=50, choices=USER_TYPES)
    
    def __str__(self):
        return self.username