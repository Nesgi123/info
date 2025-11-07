import requests

# Practical 6 - Weather Report

def get_weather(city):
    API_KEY = "0917aee4debeeb0c3259bbda3613b319"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    temperature = data['main']['temp']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']
    weather = data['weather'][0]['main']

    print(f"\nWeather Report for {city.capitalize()}")
    print(f"Temperature : {temperature}°C")
    print(f"Wind Speed : {wind_speed} m/s")
    print(f"Condition : {weather}")
    print(f"Description : {description.capitalize()}")


city_name = input("Enter city name: ")
get_weather(city_name)
