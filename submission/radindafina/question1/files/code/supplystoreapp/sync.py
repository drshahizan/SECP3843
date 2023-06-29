from pymongo import MongoClient
from .models import Sale, CustomUser

def sync_mysql_to_mongodb_sale(sale_instance):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['AA']
    collection = db['sale']

    # Create or update the document in MongoDB
    collection.update_one({'_id': sale_instance._id}, {'$set': sale_instance.__dict__}, upsert=True)

def sync_mysql_to_mongodb_customuser(customuser_instance):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['AA']
    collection = db['customuser']

    # Create or update the document in MongoDB
    collection.update_one({'_id': customuser_instance.id}, {'$set': customuser_instance.__dict__}, upsert=True)
