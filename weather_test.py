import requests

reqUrl = "https://api.open-meteo.com/v1/forecast"

leeds_forecast = {
    "latitude": 53.7965,
    "longitude": -1.5478,
    "duration_days": 14,
    "forecast_start_date": "2024-11-27",
    "forecast_end_date": "2024-11-28"
}

query_parameters = {
    "latitude": leeds_forecast["latitude"],
    "longitude": leeds_forecast["longitude"],
    "daily": "weather_code",
    "timezone": "Europe/London",
    # "forecast_days": leeds_forecast["duration_days"],
    "start_date": leeds_forecast["forecast_start_date"],
    "end_date": leeds_forecast["forecast_end_date"]
}

response = requests.get(reqUrl, params = query_parameters)

weather_code_dictionary = {
    0: "Clear sky",
    1: "Mainly clear", 
    2: "Partly cloudy", 
    3: "Overcast",
    45: "Fog", 
    48:	"Depositing rime fog",
    51: "Light Drizzle", 
    53: "Moderate Drizzle",
    55: "Dense Drizzle",
    56: "Light Freezing Drizzle", 
    57: "Dense Freezing Drizzle",
    61: "Rain",
    63: "Rain Slight",
    65: "Rain moderate and heavy intensity",
    66: "Freezing Rain",
    67:	"Freezing Rain: Light and heavy intensity",
    71: "Snow fall:Slight",
    73: "Snow fall: moderate",
    75:	"Snow fall: heavy intensity",
    77:	"Snow grains",
    80: "Rain showers slight",
    81: "Rain showers moderate",
    82:	"Rain showers violent",
    85: "Snow showers slight",
    86:	"Snow showers heavy",
    95:	"Thunderstorm: Slight or moderate",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}

weather_codes = response.json()['daily']['weather_code']
dates = response.json()['daily']['time']

print(weather_codes)
print(dates)

todays_weather_code = weather_codes[0]

todays_weather_forecast = weather_code_dictionary[todays_weather_code]

print(todays_weather_forecast)

tomorrows_weather_code = weather_codes[1]

tomorrows_weather_forecast = weather_code_dictionary[tomorrows_weather_code]

print(tomorrows_weather_forecast)

