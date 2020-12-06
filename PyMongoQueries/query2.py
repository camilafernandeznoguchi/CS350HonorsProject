#Find all clients who have bought more than 1 mattress in the same order

import pymongo
from pymongo import MongoClient
import time

cluster = MongoClient("mongodb+srv://admin:1234@cluster0.pr9uk.mongodb.net/DrimerDB?retryWrites=true&w=majority")
db = cluster["DimerDB"]
OrderCollection = db["Order"]

start_time = time.time()

resultlist = []
counter = 0
for result in OrderCollection.aggregate([
        {
            '$lookup':
            {
                'from': "Product",
                'localField': "product.product_id",
                'foreignField': "_id",
                'as': "result_docs"
            }
        }
    ]):
    mattress_perorder = 0
    for product in result['result_docs']:
        if product['type'] == 'mattress':
            mattress_perorder += 1
        if mattress_perorder > 1:
            counter += 1
            resultlist.append(result['client_id'])
            break

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))

resultlist.sort()
for item in resultlist:
    print(resultlist)
print("Total Rows: ", counter)