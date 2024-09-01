# python-scripts/weather.py

import requests
import sys
import json

def fetch_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    api_key = sys.argv[1]
    city = sys.argv[2]
    weather_data = fetch_weather(api_key, city)
    print(json.dumps(weather_data))
