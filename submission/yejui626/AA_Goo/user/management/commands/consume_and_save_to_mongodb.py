from django.core.management.base import BaseCommand
from kafka import KafkaConsumer
from pymongo import MongoClient
from django.forms.models import model_to_dict
from user.models import Story
import json

class Command(BaseCommand):
    help = 'Consume data from Kafka and save it to MongoDB'

    def handle(self, *args, **options):
        # Connect to Kafka
        consumer = KafkaConsumer(
            'story-events',
            bootstrap_servers=['localhost:9092'],
            group_id=None,
            auto_offset_reset='earliest',
        )

        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017')
        db = client['AA']
        collection = db['stories_story']

        # Consume messages from Kafka and save to MongoDB
        for message in consumer:
            data = message.value.decode('utf-8')  # Decode the bytes to a string
            data_dict = json.loads(data)  # Parse the JSON string to a dictionary
            
            # Exclude the ModelState field
            data_dict.pop('_state', None)
            
            story = Story(**data_dict)  # Create a Story object using the dictionary
            story_dict = model_to_dict(story)  # Convert the Story object to a dictionary
            collection.insert_one(story_dict)

        # Close connections
        consumer.close()
        client.close()
