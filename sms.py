import sys
import os
import hashlib
import hmac
import base64
import requests
import time
import json


def make_signature(string, api_key) :
	secret_key_org = api_key["key"]
	secret_key = bytes(secret_key_org, 'UTF-8')
	string = bytes(string, 'UTF-8')
	string_hmac = hmac.new(secret_key, string, digestmod=hashlib.sha256).digest()
	string_base64 = base64.b64encode(string_hmac).decode('UTF-8')
	return string_base64


def sendSMS() :
	api_key = ""
	uri = ""
	with open("key.json") as key_file:
		api_key = json.load(key_file)
	timestamp = str(int(time.time() * 1000))
	url = "https://sens.apigw.ntruss.com"
	uri = api_key["uri"]
	api_url = url + uri
	access_key = "Ajy5izUT3YteMFsq8B95"
	string_to_sign = "POST " + uri + "\n" + timestamp + "\n" + access_key

#make signature
	signature = make_signature(string_to_sign, api_key)

	headers = {
		'Content-Type' : 'application/json; charset=utf-8',
		'x-ncp-apigw-timestamp' : timestamp,
		'x-ncp-iam-access-key' : access_key,
		'x-ncp-apigw-signature-v2' : signature
	}

	body = {
		"type" : "SMS",
		"contentType": "COMM",
		"from" : "01074145644",
		"content": "맥북 픽업 물량 풀림!",
		"messages" : [{"to" : "01074145644"}]
	}

	body = json.dumps(body)

	response = requests.post(api_url, headers=headers, data=body)
	response.raise_for_status()



	

