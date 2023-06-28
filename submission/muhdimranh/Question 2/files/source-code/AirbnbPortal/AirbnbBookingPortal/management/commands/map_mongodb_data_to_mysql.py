from datetime import datetime
import decimal
from decimal import Decimal

from django.core.management.base import BaseCommand
from AirbnbBookingPortal.models import ListingAndReviews
import pymongo

def retrieve_data_from_mongodb():
    # MongoDB connection details
    host = 'mongodb+srv://muhdimranh:123@sentimentanalysis.5esk2hq.mongodb.net/'
    database_name = 'airbnbportal'
    collection_name = 'ListingsAndReviews'

    # Connect to MongoDB
    client = pymongo.MongoClient(host)
    database = client[database_name]
    collection = database[collection_name]

    # Retrieve all documents from the collection
    documents = collection.find()

    # Convert MongoDB documents to a list of dictionaries
    data = list(documents)

    return data


def map_mongodb_data_to_mysql():
    # Connect to MongoDB and retrieve the data
    mongodb_data = retrieve_data_from_mongodb()

    # Iterate over the MongoDB data
    for document in mongodb_data:
        # Map the fields to the corresponding Django model attributes
        listing = ListingAndReviews(
            id=document.get('_id', ''),
            listing_url=document.get('listing_url', ''),
            name=document.get('name', ''),
            summary=document.get('summary', ''),
            interaction=document.get('interaction', ''),
            house_rules=document.get('house_rules', ''),
            property_type=document.get('property_type', ''),
            room_type=document.get('room_type', ''),
            bed_type=document.get('bed_type', ''),
            minimum_nights=document.get('minimum_nights', ''),
            maximum_nights=document.get('maximum_nights', ''),
            cancellation_policy=document.get('cancellation_policy', ''),
            last_scraped=document.get('last_scraped', ''),
            calendar_last_scraped=document.get('calendar_last_scraped', ''),
            first_review=document.get('first_review', ''),
            last_review=document.get('last_review', ''),
            accommodates=document.get('accommodates', ''),
            bedrooms=document.get('bedrooms', ''),
            beds=document.get('beds', ''),
            number_of_reviews=document.get('number_of_reviews', ''),
            bathrooms=document.get('bathrooms', ''),
            amenities=document.get('amenities', ''),
            price=document.get('price', ''),
            security_deposit=document.get('security_deposit', ''),
            cleaning_fee=document.get('cleaning_fee', ''),
            extra_people=document.get('extra_people', ''),
            guests_included=document.get('guests_included', ''),
            images=document.get('images', ''),
            host=document.get('host', ''),
            address=document.get('address', ''),
            availability=document.get('availability', ''),
            review_scores=document.get('review_scores', ''),
            reviews=document.get('reviews', '')
        )
        # Convert date strings to proper format
    if 'first_review' in document and document['first_review']:
        first_review = document['first_review'].strftime('%Y-%m-%d')
        listing.first_review = datetime.strptime(first_review, '%Y-%m-%d').date()

    if 'last_review' in document and document['last_review']:
        last_review = document['last_review'].strftime('%Y-%m-%d')
        listing.last_review = datetime.strptime(last_review, '%Y-%m-%d').date()

    # Convert the 'bathrooms' value to a decimal
    if 'bathrooms' in document and document['bathrooms']:
        bathrooms = Decimal(str(document['bathrooms']))
        listing.bathrooms = bathrooms

       # Convert price to a decimal
    
    if 'price' in document and document['price']:
        price_str = str(document['price']).replace(',', '').strip()  # Remove commas and whitespace
        print('Price value:', price_str)
        price_decimal = Decimal(price_str)
        listing.price = price_decimal


        # Save the listing object to MySQL
        listing.save()

    print('Data migration from MongoDB to MySQL completed successfully.')



class Command(BaseCommand):
    help = 'Map MongoDB data to MySQL'

    def handle(self, *args, **options):
        map_mongodb_data_to_mysql()
