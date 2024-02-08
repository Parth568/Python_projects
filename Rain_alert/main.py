import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "ENTER THE API KEY"
account_sid = "ENTER THE TWILIO SID"
auth_token = "ENTER THE TWILIO AUTH TOKEN"
from_Sender_number = "ENTER THE TWILIO NO."
to_receiver_number = "ENTER YOUR MOBILE NO."


weather_params = {
    "lat": ENTER your lat,
    "lon": Enter your lon,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an ☂️",
                from_=from_Sender_number,
                to=to_receiver_number)
    print(message.status)
