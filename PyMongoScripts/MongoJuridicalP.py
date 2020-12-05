import csv
import time
import pymongo
from pymongo import MongoClient

start_time = time.time()

cluster = MongoClient("mongodb+srv://admin:1234@cluster0.pr9uk.mongodb.net/DrimerDB?retryWrites=true&w=majority")
db = cluster["DimerDB"]
collection = db["JuridicalPerson"]

mylist = []

with open('/data/personaJuridica_1000.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    linecount = 0
    for row in myreader:
        mylist.insert(linecount, {"_id": int(row[0]), "name": row[1], "address": row[2], "representative_id": int(row[3]), "phone": int(row[4])})
        linecount += 1

collection.insert_many(mylist)

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))