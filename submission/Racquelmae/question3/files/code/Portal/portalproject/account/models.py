from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField('Is customer', default=False)
    is_technical = models.BooleanField('Is technical', default=False)
    is_senior = models.BooleanField('Is senior', default=False)
