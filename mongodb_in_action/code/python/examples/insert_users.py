from pymongo import MongoClient

# Connect to Mongo
client = MongoClient('localhost', 27017)

# Use database
db = client.tutorial

# Insert some users
smith_id = db.users.insert_one({'username': 'smith'})
jones_id = db.users.insert_one({'username': 'jones'})