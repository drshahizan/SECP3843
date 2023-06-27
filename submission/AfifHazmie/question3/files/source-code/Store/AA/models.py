from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class JSONData(models.Model):
    data = models.JSONField()

import json
from AA.models import JSONData

def load_json_data():
    with open('sales.json') as f:
        json_data = json.load(f)
    JSONData.objects.create(data=json_data)

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_technical_worker = models.BooleanField(default=False)
    is_senior_management = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')

    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')