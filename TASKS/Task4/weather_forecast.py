import requests

API_KEY = "YOUR_API_HERE"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather_by_city(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric" 
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()


def get_weather_by_zip(zip_code):
    params = {
        "zip": zip_code,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()


def display_weather(data):
    """Extract and display relevant weather information."""
    if data.get("cod") != 200:
        print("\nError:", data.get("message", "Unable to fetch weather data."))
        return

    city = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    print("\n" + "="*40)
    print(f" Weather Report for {city}, {country}")
    print("="*40)
    print(f" Temperature : {temperature}°C")
    print(f" Humidity    : {humidity}%")
    print(f" Wind Speed  : {wind_speed} m/s")
    print(f" Conditions  : {description.capitalize()}")
    print("="*40)


def main():
    print("=== Weather Forecast Application ===")
    user_input = input("Enter city name or ZIP code: ").strip()

    if user_input.isdigit():
        weather_data = get_weather_by_zip(user_input)
    else:
        weather_data = get_weather_by_city(user_input)

    display_weather(weather_data)


if __name__ == "__main__":
    main()
