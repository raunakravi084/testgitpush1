import pymongo

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://root:root@cluster0.zujon.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client.test
print(db)

d = {
    "name":'Raunak',
    "email":'raunak@gmail.com',
    'surname':'ravi'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)