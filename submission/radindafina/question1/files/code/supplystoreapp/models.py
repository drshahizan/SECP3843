from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Sale(models.Model):
    _id = models.CharField(max_length=255, primary_key=True)
    saleDate = models.DateTimeField(db_column='sale_date')  # Rename field to match JSON key
    storeLocation = models.CharField(max_length=100, db_column='store_location')  # Rename field to match JSON key
    customerGender = models.CharField(max_length=1, db_column='customer_gender')  # Rename field to match JSON key
    customerAge = models.PositiveIntegerField(db_column='customer_age')  # Rename field to match JSON key
    customerEmail = models.EmailField(db_column='customer_email')  # Rename field to match JSON key
    satisfaction = models.PositiveSmallIntegerField()
    couponUsed = models.BooleanField(db_column='couponUsed')  # Rename field to match JSON key
    purchaseMethod = models.CharField(max_length=100, db_column='purchase_method')  # Rename field to match JSON key

class CustomUser(AbstractUser):
    customer = models.BooleanField(default=False)
    technical_worker = models.BooleanField(default=False)
    senior_management = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')
