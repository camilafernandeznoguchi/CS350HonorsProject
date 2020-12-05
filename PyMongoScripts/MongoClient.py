import csv
import time
import pymongo
from pymongo import MongoClient

start_time = time.time()

cluster = MongoClient("mongodb+srv://admin:1234@cluster0.pr9uk.mongodb.net/DrimerDB?retryWrites=true&w=majority")
db = cluster["DimerDB"]
collection = db["Client"]

clientlist = []

with open('/data/cliente_1000.csv', newline='') as csvfile:
    clientereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    linecount = 0
    for row in clientereader:
        clientlist.insert(linecount, {"_id": int(row[0]), "name": row[1],"surname": row[2], "address": row[3], "phone": int(row[4])})
        linecount += 1

collection.insert_many(clientlist)

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))