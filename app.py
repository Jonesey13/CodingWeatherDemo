from flask import Flask, render_template
from weather_codes import weather_code_dictionary

app = Flask(__name__)

@app.route("/")
def hello_world():
    import requests

    reqUrl = "https://api.open-meteo.com/v1/forecast"

    leeds_forecast = {
        "latitude": 53.7965,
        "longitude": -1.5478,
        "duration_days": 14
    }

    query_parameters = {
        "latitude": leeds_forecast["latitude"],
        "longitude": leeds_forecast["longitude"],
        "daily": "weather_code",
        "timezone": "Europe/London",
        "forecast_days": leeds_forecast["duration_days"]
    }

    response = requests.get(reqUrl, params = query_parameters)

    weather_code_dictionary 

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

    return render_template("weather.html", todays_forecast = todays_weather_forecast, tomorrows_forecast = tomorrows_weather_forecast)