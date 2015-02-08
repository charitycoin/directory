import os
import sys
import json
import requests
import base64
from requests.auth import HTTPBasicAuth


dbname = os.getenv("cc_dbname") # nonprofits
baseurl = os.getenv("cc_baseurl") # adrianparsons.cloudant.com/
username = os.getenv("cc_username") # configured in couchdb
password = os.getenv("cc_password") # ditto

jsonfile = sys.argv[1]

headers = {
	"Content-Type" : "application/json"
}

url = baseurl + "/" + dbname

jsonblob = open(jsonfile)
jsonstring = jsonblob.read()
jsondata = json.loads(jsonstring)

jsondata["_id"] = jsondata["ein"]

res = requests.post(url, auth=HTTPBasicAuth(username, password), data=json.dumps(jsondata), headers=headers)
print res.text