import requests
import json

def get_forecast(user_agent, latitude, longitude):

    #request to get local station

    #make a request
    coords_endpoint = f"https://api.weather.gov/points/{latitude},{longitude}"
    headers = {
        'user-agent': user_agent,
        'accept': 'application/geo+json'
    }
    r = requests.get(coords_endpoint, headers=headers)

    #request to get forecast
    response = json.loads(r.text)
    station = response["properties"]["cwa"]
    gridX = response["properties"]["gridX"]
    gridY = response["properties"]["gridY"]
    print(f"{station}: {gridX}, {gridY}")

    forecast_endpoint = f"https://api.weather.gov/gridpoints/{station}/{gridX},{gridY}/forecast"
    r = requests.get(forecast_endpoint, headers=headers)

    #construct forecast from request
    forecast_response = json.loads(r.text)['properties']['periods']
    forecast = []
    for response in forecast_response:
        forecast.append({
            'name': response['name'],
            'temperature': response['temperature'],
            'wind_info': f"{response['windSpeed']} {response['windDirection']}",
            'icon': response['icon'],
            'detailed_forecast': response['detailedForecast'],
            })

    return forecast