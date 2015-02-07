import json
import os
import requests

# list files in orgs directory
file_list = os.listdir("orgs")

# move to orgs directory
os.chdir("orgs")

for single_file in file_list:

	temp_file  = open(single_file)
	print temp_file
	temp_content = temp_file.read()
	temp_json = json.loads(temp_content)

	print temp_json

	if "coinbase" in temp_json['payments']:
		temp_address = temp_json['payments']['coinbase']['address']
		temp_confirm = temp_json['payments']['coinbase']['confirmation']
	elif "bitcoin" in temp_json['payments']:
		temp_address = temp_json['payments']['bitcoin']['address']
		temp_confirm = temp_json['payments']['bitcoin']['confirmation']
	else:
		print "there was a problem"
	
	http_test = requests.get(temp_confirm)
	if temp_address in http_test.text:
		print "success!"
	else:
		print "failure! in ", single_file


