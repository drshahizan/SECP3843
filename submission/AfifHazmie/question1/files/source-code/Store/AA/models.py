from django.db import models

# Create your models here.
from django.db import models

class JSONData(models.Model):
    data = models.JSONField()

import json
from AA.models import JSONData

def load_json_data():
    with open('sales.json') as f:
        json_data = json.load(f)
    JSONData.objects.create(data=json_data)