# extract value(s) from key's in dictionary

import urllib.request
import json
import datetime as dt


def extract_data():
    with urllib.request.urlopen('https://api.weather.gov/gridpoints/RAH/61%2c55/forecast') as url:
        data = json.load(url)
        iso_date = dt.datetime.fromisoformat(
            data['properties']['periods'][0]['endTime'])
        utc_date = iso_date.strftime('%b %d, %Y')
        time_of_day = data['properties']['periods'][0]['name']
        temp = data['properties']['periods'][0]['temperature']
        sf = data['properties']['periods'][0]['shortForecast']
        df = data['properties']['periods'][0]['detailedForecast']
        weather_report = (
            f"This is a weather report for North Raleigh: \n\nDate of forecast: {utc_date}\nTime of Day: {time_of_day} \nTemperature: {temp} \nShort Forecast: {sf} \nDetailed Forecast: {df}")

    with open("weather.txt", "w") as outfile:
        outfile.write(weather_report)
