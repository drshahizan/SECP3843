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
