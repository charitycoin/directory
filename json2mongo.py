import os
import sys
import json
from pymongo import MongoClient

configfile = sys.argv[1]
config = json.load(open(configfile))

dbname = config["dbname"]
baseurl = config["baseurl"]

client = MongoClient(baseurl)
db = client[dbname]

collection = db["orgs"]
files = os.listdir("orgs");

collection.remove()

for jsonfile in files:
	jsonblob = open("orgs/%s" % jsonfile)
	jsonstring = jsonblob.read()
	jsondata = json.loads(jsonstring)
	jsondata["_id"] = jsondata["ein"]

	collection.insert(jsondata)
	