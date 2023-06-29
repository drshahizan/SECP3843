from django.core.management.base import BaseCommand
import json
from tweets.models import Tweet
from datetime import datetime

class Command(BaseCommand):
    help = 'Loads JSON data into the Tweet model'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                created_at = datetime.strptime(item['created_at'], "%a %b %d %H:%M:%S %z %Y").strftime("%Y-%m-%d %H:%M:%S")
                tweet = Tweet(
                    _id=item['_id'],
                    text=item['text'],
                    in_reply_to_status_id=item['in_reply_to_status_id'],
                    retweet_count=item['retweet_count'],
                    contributors=item['contributors'],
                    created_at=created_at,
                    geo=item['geo'],
                    source=item['source'],
                    coordinates=item['coordinates'],
                    in_reply_to_screen_name=item['in_reply_to_screen_name'],
                    truncated=item['truncated'],
                    entities=item['entities'],
                    retweeted=item['retweeted'],
                    place=item['place'],
                    user=item['user'],
                    favorited=item['favorited'],
                    in_reply_to_user_id=item['in_reply_to_user_id'],
                    id=item['id']
                )
                tweet.save()
                tweet.save(using='mongodb')
                self.stdout.write(self.style.SUCCESS(f'Successfully loaded data for tweet with id {tweet.id}'))
