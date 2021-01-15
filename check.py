import requests
import json
import sms
import time
from pytz import timezone
from datetime import datetime

url = "https://www.apple.com/kr/shop/retail/pickup-message?pl=true&searchNearby=true&store=R692&parts.=MGNA3KH/A"

response = requests.get(url).json()
store = response['body']['stores'][0]
reservationUrl = store['reservationUrl']
availability = store['partsAvailability']['MGNA3KH/A']['storeSelectionEnabled']
text = store['partsAvailability']['MGNA3KH/A']['storePickupQuote']

if availability:
	sms.sendSMS()
	print("true " + datetime.now(timezone('Asia/Seoul')).strftime('%c') + '\n')
else :
	print("false " + datetime.now(timezone('Asia/Seoul')).strftime('%c') + '\n')
