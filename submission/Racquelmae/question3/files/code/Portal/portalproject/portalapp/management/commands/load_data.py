from django.core.management.base import BaseCommand
import json
from portalapp.models import City

class Command(BaseCommand):
   help = 'Loads JSON data into the AA model'

   def add_arguments(self, parser):
       parser.add_argument('json_file', type=str, help='Path to the JSON file')

   def handle(self, *args, **options):
       json_file = options['json_file']
       with open(json_file, encoding='utf-8') as f:
           data = json.load(f)
           for item in data:
               city = City(
                   _id=item['_id'],
                   id=item['id'],
                   certificate_number=item['certificate_number'],
                   business_name=item['business_name'],
                   date=item['date'],
                   result=item['result'],
                   sector=item['sector'],
                   address=item['address'],
               )
               city.save()
               city.save(using='mongodb')
               self.stdout.write(self.style.SUCCESS(f'Successfully loaded data for city with id {city.id}'))