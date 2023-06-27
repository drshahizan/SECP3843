from django.db import models

class City(models.Model):
    _id = models.CharField(max_length=255, primary_key=True)
    id = models.CharField(max_length=255)
    certificate_number = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255, null=True)
    date = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    sector = models.CharField(max_length=255, null=True)
    address = models.JSONField()
