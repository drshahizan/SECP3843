from django.core.management.base import BaseCommand
from kafka import KafkaConsumer
from pymongo import MongoClient
from django.forms.models import model_to_dict
from stories.models import Story
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

        # Consume messages from Kafka and save to MongoDB
        for message in consumer:
            data = message.value.decode('utf-8')  # Decode the bytes to a string
            data_dict = json.loads(data)  # Parse the JSON string to a dictionary
            # Exclude the ModelState field
            data_dict.pop('_state', None)

            # Get the document id
            document_id = data_dict.get('id')

            # Check if a document with the same id already exists in the collection
            existing_story = db.stories_story.find_one({'id': document_id})
            existing_story_1 = db.stories_story_1.find_one({'id': document_id})
            if not existing_story:
                data_dict['replica'] = None
            elif not existing_story_1:
                data_dict['replica'] = 1
            else:
                data_dict['replica'] = 2

            story = Story(**data_dict)  # Create a Story object using the dictionary
            story_dict = model_to_dict(story)  # Convert the Story object to a dictionary

            # Get the replica information
            replica = data_dict.get('replica')

            # Determine the collection name based on the replica information
            if replica:
                collection_name = f'stories_story_{replica}'
            else:
                collection_name = 'stories_story'

            collection = db[collection_name]
            collection.insert_one(story_dict)

        # Close connections
        consumer.close()
        client.close()
