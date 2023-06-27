from django.core.management.base import BaseCommand
from django.conf import settings
from confluent_kafka import Producer, KafkaError
import json
from user.models import Story

class Command(BaseCommand):
    help = 'Send data from Story model to Kafka topic'

    def handle(self, *args, **options):
        KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'  # Update with your Kafka bootstrap servers

        # Kafka Producer configuration
        producer_config = {
            'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
            'client.id': 'mysql_to_mongodb_producer',  # Update with a unique client ID
        }

        # Create Kafka producer instance
        producer = Producer(producer_config)

        # Fetch data from the Story model
        stories = Story.objects.all()

        # Loop over the stories and send them to Kafka
        for story in stories:
            # Prepare the data to be sent to Kafka
            data = {
                'id': story.id,
                'href': story.href,
                'title': story.title,
                'comments': story.comments,
                'container': story.container,
                'submit_date': story.submit_date.isoformat(),
                'topic': story.topic,
                'promote_date': story.promote_date.isoformat(),
                'idJSON': story.idJSON,
                'media': story.media,
                'diggs': story.diggs,
                'description': story.description,
                'link': story.link,
                'user': story.user,
                'status': story.status,
                'shorturl': story.shorturl,
            }

            # Convert the data to JSON string
            json_data = json.dumps(data)

            # Send the JSON data to the Kafka topic using the producer
            producer.produce(topic="story-events", value=json_data)

            # Poll the producer to trigger delivery reports
            producer.poll(0)

        # Flush the producer to ensure all messages are sent
        producer.flush()

        producer.close()

