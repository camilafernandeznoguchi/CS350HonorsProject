# Find which store has the most stock of the product with id = 2115020691

import pymongo
from pymongo import MongoClient
import pprint
import time

cluster = MongoClient("mongodb+srv://admin:1234@cluster0.pr9uk.mongodb.net/DrimerDB?retryWrites=true&w=majority")
db = cluster["DimerDB"]
collection = db["Store"]

start_time = time.time()

results = {}

for store in collection.find(
  {"product.product_id": "2115020691"},
  {"product": {"$elemMatch": {"product_id": "2115020691"}}
  }):
  results[store["_id"]] = store["product"][0]["stock"]

maximum = max(results, key=results.get)
print("store_id: ", maximum)

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))