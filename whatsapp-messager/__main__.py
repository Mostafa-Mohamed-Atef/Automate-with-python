import pywhatkit
import json 
from datetime import datetime, timedelta
import time 

tomorrow = datetime.now() + timedelta(days=1)

TOMORROW_DATE = tomorrow.strftime("%m-%d")
print(TOMORROW_DATE)
with open("whatsapp-messager/contact.json") as file:
    contact = json.load(file)

for date, people in contact.items():
    if date == TOMORROW_DATE:
        for num, msg in people.items():
            now = datetime.now()
            hr = now.hour
            min = now.minute + 2
            if min >= 60:
                hr += 1
                min -= 60
            try:
                print(f"sending message to {num}")
                pywhatkit.sendwhatmsg(num, msg, hr, min)
                time.sleep(20)
            except Exception as e:
                print(e)
    else:
        print("No Birthdays Tomorrow")
