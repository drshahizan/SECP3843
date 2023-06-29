from django.db import connections
from pymongo import MongoClient

# Establish connections to MySQL and MongoDB
mysql_connection = connections['default']
mongodb_client = MongoClient('mongodb+srv://cluster0.cpy5tdw.mongodb.net', username='peiyu', password='1')

# Perform a dual write to MySQL and MongoDB
def dual_write(tweet_data):
    try:
        # Insert into MySQL
        mysql_cursor = mysql_connection.cursor()
        mysql_query = """
            INSERT INTO tweets_tweet (_id, text, in_reply_to_status_id, retweet_count, contributors,
            created_at, geo, source, coordinates, in_reply_to_screen_name, truncated, entities, retweeted,
            place, user, favorited, in_reply_to_user_id, id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        mysql_values = (
            tweet_data['_id'], tweet_data['text'], tweet_data['in_reply_to_status_id'],
            tweet_data['retweet_count'], tweet_data['contributors'], tweet_data['created_at'],
            tweet_data['geo'], tweet_data['source'], tweet_data['coordinates'],
            tweet_data['in_reply_to_screen_name'], tweet_data['truncated'], tweet_data['entities'],
            tweet_data['retweeted'], tweet_data['place'], tweet_data['user'], tweet_data['favorited'],
            tweet_data['in_reply_to_user_id'], tweet_data['id']
        )
        mysql_cursor.execute(mysql_query, mysql_values)

        # Insert into MongoDB
        mongodb_db = mongodb_client['AA']
        mongodb_collection = mongodb_db['tweet']
        mongodb_collection.insert_one(tweet_data)

        print("Dual write successful!")

    except Exception as e:
        print(f"Dual write failed: {str(e)}")


