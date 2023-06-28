from django.db import models

# Create your models here.
class Account(models.Model):
    account_id = models.IntegerField(primary_key=True)
    limit = models.IntegerField()
    products = models.JSONField()
    
    def __str__(self):
        return f"Account ID: {self.account_id}"
    
class Customer(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.TextField()
    birthdate = models.DateTimeField()
    email = models.EmailField()
    active = models.BooleanField()
    accounts = models.JSONField()
    tier_and_details = models.JSONField()

    def __str__(self):
        return self.username


class Transaction(models.Model):
    account_id = models.IntegerField()
    transaction_count = models.IntegerField()
    bucket_start_date = models.DateTimeField()
    bucket_end_date = models.DateTimeField()
    transactions = models.JSONField()

    def __str__(self):
        return f"Transactions for Account ID: {self.account_id}"