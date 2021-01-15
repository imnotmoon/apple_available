import requests
import json
import sms
import time
import sys
from pytz import timezone
from datetime import datetime

device = sys.argv[1]

url = "https://www.apple.com/kr/shop/retail/pickup-message?pl=true&searchNearby=true&store=R692&parts.=" + device

response = requests.get(url).json()
store = response['body']['stores'][0]
reservationUrl = store['reservationUrl']
availability = store['partsAvailability'][device]['storeSelectionEnabled']
text = store['partsAvailability'][device]['storePickupQuote']

if availability:
	sms.sendSMS()
	print("true " + datetime.now(timezone('Asia/Seoul')).strftime('%c') + '\n')
else :
	print("false " + datetime.now(timezone('Asia/Seoul')).strftime('%c') + '\n')
