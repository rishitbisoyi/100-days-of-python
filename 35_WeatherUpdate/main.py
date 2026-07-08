import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "OWM_API_KEY"
account_sid = "TWILIO_ACCOUNT_ID"
auth_token = "TWILIO_AUTH_TOKEN"

params = {
    "lat": "12.872140",
    "lon": "80.106789",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="TWILIO VIRTUAL NUMBER",
        to="TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)