import requests
import json
from datetime import date  
from datetime import timedelta  
from time import sleep
from notifypy import Notify

while True:
    districtID = 294

    today = date.today()
    for i in range(8):
        dt = today + timedelta(days=i)
        strDate = dt.strftime("%d-%m-%Y")
        url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=' + str(districtID) + '&date=' + strDate
        try:
            response = requests.get(url)
            response.raise_for_status()
            responseJSON = response.json()
        except requests.HTTPError as e:
            print('Cowin Server is Down - ', e)
            sleep(5)
            continue

        sessions = responseJSON['sessions']

        for session in sessions:
            if session['min_age_limit'] == 18 and session['available_capacity'] > 1:
                print(str(session['available_capacity']) + 'doses of' + session['vaccine'] + ' available on ' + dt.strftime("%A %d %B %Y") + ' at ' + session['name'])
                notification = Notify()
                notification.title = session['vaccine'] + " Slot Found!"
                notification.message = session['vaccine'] + ' available on ' + dt.strftime("%A %d. %B %Y") + ' at ' + session['name']
                notification.send()
    
    sleep(2)