import requests
import os
from twilio.rest import Client


key = os.environ.get('API_KEY')
lat = '30.438255'
lon = '-84.280731'
acc_sid = os.environ.get('ACC_SID')
auth_token = os.environ.get('AUTH_TOKEN')


params = {
    'appid': key,
    'lat': lat,
    'lon': lon,
    'exclude': 'daily,minutely,current'
}


r = requests.get(
    f'https://api.openweathermap.org/data/2.5/onecall', params=params)
r.raise_for_status()
weather_data = r.json()
slice = weather_data['hourly'][:11]

will_rain = False

for hour_data in slice:
    condition_code = int(hour_data['weather'][0]['id'])
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(acc_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today! Don't forget an umbrella ☔",
            from_='+1(TWILIO NUMBER)',
            to='+1(YOUR PHONE NUMBER)'
        )
    print(message.status)

####
# I currently have this service running on PythonAnywhere
