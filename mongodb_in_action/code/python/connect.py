from pymongo import MongoClient
import pprint

# Connect to Mongo
client = MongoClient('localhost', 27017)

# Use database
db = client.tutorial

# Show collections
print('Collections:')
for c in db.list_collection_names():
    print(c)

# Use collection
users = db.users

# Show users
print('Users:')
for u in users.find():
    pprint.pprint(u)