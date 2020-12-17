from pymongo import MongoClient

# Connect to Mongo
client = MongoClient('localhost', 27017)

# Use database
db = client.tutorial

# Delete a single document
db.users.delete_one({'username': 'smith'})

# Delete existing documents in users collection
db.users.delete_many({})