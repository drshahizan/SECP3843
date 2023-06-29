import json
from django.core.management.base import BaseCommand
from supplystoreapp.models import Sale
from datetime import datetime

class Command(BaseCommand):
    help = 'Load data from JSON file into Sale model'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']
        with open(json_file) as f:
            data = json.load(f)

        for item in data:
            sale_date = item['saleDate']['$date']
            if isinstance(sale_date, dict):
                # Check if sale_date is a dictionary
                sale_date = sale_date['$numberLong']
            sale_date = int(sale_date) / 1000

            sale = Sale()
            sale._id = item['_id']['$oid']
            sale.saleDate = datetime.fromtimestamp(sale_date)
            sale.storeLocation = item['storeLocation']
            sale.customerGender = item['customer']['gender']
            sale.customerAge = int(item['customer']['age']['$numberInt'])
            sale.customerEmail = item['customer']['email']
            sale.satisfaction = int(item['customer']['satisfaction']['$numberInt'])
            sale.couponUsed = item['couponUsed']
            sale.purchaseMethod = item['purchaseMethod']
            sale.save()

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
