import csv
import time
import pymongo
from pymongo import MongoClient

start_time = time.time()

cluster = MongoClient("mongodb+srv://admin:1234@cluster0.pr9uk.mongodb.net/DrimerDB?retryWrites=true&w=majority")
db = cluster["DimerDB"]
collection = db["Store"]

mylist = []

with open('/data/store.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    linecount = 0
    for row in myreader:
        templist = []
        mylist.insert(linecount, {"_id": int(row[0]), "address": row[1], "product": templist})
        linecount += 1

with open('/data/Catalogo.csv', newline='') as csvfile2:
    cataloguereader = csv.reader(csvfile2, delimiter=',', quotechar='"')
    for catalogueentry in cataloguereader:
        listindex = int(catalogueentry[1])-1
        mylist[listindex]["product"].append({"product_id": catalogueentry[0], "stock": int(catalogueentry[2])})

collection.insert_many(mylist)

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))