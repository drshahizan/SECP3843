from django.core.management.base import BaseCommand
import json
from user.models import Story
from datetime import datetime, timezone

class Command(BaseCommand):
    help = 'Loads JSON data into the Story model'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')
    
    def extract_integer_value(self, value):
        if isinstance(value, dict) and "$numberInt" in value:
            return int(value["$numberInt"])
        return value
    
    def extract_datetime_value(self, value):
        if isinstance(value, dict) and "$numberInt" in value:
            unix_timestamp = int(value["$numberInt"])
            return datetime.utcfromtimestamp(unix_timestamp).replace(tzinfo=timezone.utc)
        return value

    def handle(self, *args, **options):
        json_file = options['json_file']
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                comments_m = self.extract_integer_value(item['comments'])
                diggs_m = self.extract_integer_value(item['diggs'])
                submit_date_m = self.extract_datetime_value(item['submit_date'])
                promote_date_m = self.extract_datetime_value(item['promote_date'])
                story = Story(
                    href=item['href'],
                    title=item['title'],
                    comments=comments_m,
                    container=item['container'],
                    submit_date=submit_date_m,
                    topic=item['topic'],
                    promote_date=promote_date_m,
                    idJSON=item['id'],
                    media=item['media'],
                    diggs=diggs_m,
                    description=item['description'],
                    link=item['link'],
                    user=item['user'],
                    status=item['status'],
                    shorturl=item['shorturl']
                )
                story.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully loaded data for story with id {story.id}'))
