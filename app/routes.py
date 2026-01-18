from flask import render_template
from app import app

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

    return render_template("index.html")