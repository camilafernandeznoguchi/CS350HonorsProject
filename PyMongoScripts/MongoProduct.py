import csv
import time
import pymongo
from pymongo import MongoClient

start_time = time.time()

cluster = MongoClient("mongodb+srv://admin:1234@cluster0.pr9uk.mongodb.net/DrimerDB?retryWrites=true&w=majority")
db = cluster["DimerDB"]
collection = db["Product"]

mylist = []

with open('/data/Productos.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    linecount = 0
    for row in myreader:
        mylist.insert(linecount, {"_id": row[0], "detail": row[1], "price": int(row[2])})
        linecount += 1

with open('/data/Colchones.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in myreader:
        for dictionary in mylist:
            if dictionary["_id"] == row[0]:
                linecount += 1
                dictionary["type"] = "mattress"
                dictionary["filling"] = row[1]
                dictionary["size"] = row[2]

with open('/data/Almohada.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in myreader:
        for dictionary in mylist:
            if dictionary["_id"] == row[0]:
                dictionary["type"] = "pillow"
                dictionary["filling"] = row[1]

with open('/data/Sofas.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in myreader:
        for dictionary in mylist:
            if dictionary["_id"] == row[0]:
                dictionary["type"] = "couch"
                dictionary["model"] = row[1]

collection.insert_many(mylist)

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))