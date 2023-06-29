import mysql.connector 
import pymongo
 
delete_existing_documents = True
 
mysql_host="localhost" 
mysql_database="db_mflix" 
mysql_user="root" 
mysql_password=""
 
mongodb_host = "mongodb://localhost:27017/" 
mongodb_dbname = "mflix"
mongodb_col = "accounts_user"
 
mysqldb = mysql.connector.connect( 
   host=mysql_host, 
   database=mysql_database, 
   user=mysql_user, 
   password=mysql_password 
)

mycursor = mysqldb.cursor(dictionary=True) 
mycursor.execute("SELECT * from accounts_user;") 
myresult = mycursor.fetchall()
 
myclient = pymongo.MongoClient(mongodb_host) 
mydb = myclient[mongodb_dbname] 
mycol = mydb[mongodb_col]
 
if len(myresult) > 0: 
       x = mycol.insert_many(myresult) #myresult comes from mysql cursor 
       print(len(x.inserted_ids), "inserted")