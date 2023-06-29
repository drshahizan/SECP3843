from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_technical = models.BooleanField('Is technical worker', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_senior = models.BooleanField('Is senior manager', default=False)