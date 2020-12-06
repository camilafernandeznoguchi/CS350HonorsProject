# Find all clients who have made an order after 2016

import pymongo
from pymongo import MongoClient
from datetime import datetime
import time

cluster = MongoClient("mongodb+srv://admin:1234@cluster0.pr9uk.mongodb.net/DrimerDB?retryWrites=true&w=majority")
db = cluster["DimerDB"]
collection = db["Order"]

start_time = time.time()

start = datetime(2016, 12, 31, 0, 0, 0)

for order in collection.find({'date': {'$gt': start}}, {'client_id': 1}):
    print("client_id: ", order['client_id'])

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))