import requests
import datetime as dt

# Exemple API CALL api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=d194d2ea1653c77203d20bfa402c5690

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('API KEY.txt','r').read()
CITY = "Cluj"

def kelvin_to_celsius_farenheit(kelvin):
    celsius = kelvin - 273.15
    farenheit = celsius * (9/5) + 32
    return celsius, farenheit

url = BASE_URL  + "q=" + CITY + "&APPID=" + API_KEY

response = requests.get(url).json()


temp_kelvin = response['main']['temp']
temp_celsius, temp_farenheit = kelvin_to_celsius_farenheit(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feel_like_celsius, feels_like_farenheith = kelvin_to_celsius_farenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


print(f'Temperatura in {CITY}: {temp_celsius:.2f}°C')
print(f'Temperatura resimtita in {CITY}: {feel_like_celsius:.2f}°C\n')
print(f'Umiditatea in orasul {CITY}: {humidity}%')
print(f'Viteza vantului in orasul {CITY}: {wind_speed}m/s\n')
print(f"Vreme generala {CITY}: {description}")
print(f"Rasaritul in {CITY}: {sunrise_time}")
print(f"Apusul in  {CITY}: {sunset_time}")