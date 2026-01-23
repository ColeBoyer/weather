from flask import render_template
from app import app
from api.weather import get_forecast

import requests
import json


@app.route('/')
@app.route('/index')
def index():
    coords = app.config['COORDINATES']
    user_agent = app.config['USER_AGENT']

    #make a request
    coords_endpoint = f"https://api.weather.gov/points/{coords[0]},{coords[1]}"
    headers = {
        'user-agent': user_agent,
        'accept': 'application/geo+json'
    }
    r = requests.get(coords_endpoint, headers=headers)

    #get grid points
    response = json.loads(r.text)
    station = response["properties"]["cwa"]
    gridX = response["properties"]["gridX"]
    gridY = response["properties"]["gridY"]
    print(f"{station}: {gridX}, {gridY}")

    forecast_endpoint = f"https://api.weather.gov/gridpoints/{station}/{gridX},{gridY}/forecast"
    r = requests.get(forecast_endpoint, headers=headers)
    print(r.text)

    return render_template("index.html", code=r.text)

@app.route('/dashboard')
def dashboard():

    demo_forecasts = [
        {
            'name': "Tuesday",
            'temperature': 71,
            'detailed_forecast': "Something here",
            'wind_info': "windSpeed windDirection",
            'icon': "https://api.weather.gov/icons/land/night/fog?size=medium",
        },
        {
            'name': "Tuesday",
            'temperature': 72,
            'detailed_forecast': "Something here",
            'wind_info': "windSpeed windDirection",
            'icon': "https://api.weather.gov/icons/land/night/fog?size=medium",
        },
        {
            'name': "Tuesday",
            'temperature': 73,
            'detailed_forecast': "Something here",
            'wind_info': "windSpeed windDirection",
            'icon': "https://api.weather.gov/icons/land/night/fog?size=medium",
        },
        {
            'name': "Tuesday",
            'temperature': 74,
            'detailed_forecast': "Something here",
            'wind_info': "windSpeed windDirection",
            'icon': "https://api.weather.gov/icons/land/night/fog?size=medium",
        },
        {
            'name': "Tuesday",
            'temperature': 75,
            'detailed_forecast': "Something here",
            'wind_info': "windSpeed windDirection",
            'icon': "https://api.weather.gov/icons/land/night/fog?size=medium",
        },
    ]

    forecasts = get_forecast(app.config['USER_AGENT'], app.config['COORDINATES'][0], app.config['COORDINATES'][1])

    return render_template("dashboard.html", forecasts=forecasts)