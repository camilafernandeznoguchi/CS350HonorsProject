import csv
import time
import pymongo
from pymongo import MongoClient
import datetime

start_time = time.time()

cluster = MongoClient("mongodb+srv://admin:1234@cluster0.pr9uk.mongodb.net/DrimerDB?retryWrites=true&w=majority")
db = cluster["DimerDB"]
collection = db["Order"]

mylist = []

with open('/data/Pedido_1000.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    linecount = 0
    for row in myreader:
        templist = []
        datelist = row[1].split('/')
        mydate = datetime.datetime(2000+int(datelist[2]), int(datelist[0]), int(datelist[1]))
        mylist.insert(linecount, {"_id": int(row[0]), "date": mydate, "client_id": int(row[2]), "product": templist})
        linecount += 1

with open('Tiene_1000.csv', newline='') as csvfile:
    tienereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in tienereader:
        for dictionary in mylist:
            if dictionary["_id"] == int(row[0]):
                dictionary["product"].append({"product_id": row[1], "store_id": int(row[2]), "quantity": int(row[3])})

collection.insert_many(mylist)

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))