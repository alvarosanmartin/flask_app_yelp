import forecastio
from geopy.geocoders import Nominatim
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather_from_address(address):

    api_key = os.environ['FORECASTIO_API_KEY']
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    print ("The location is {}".format(location.address))
    lat = location.latitude
    lng = location.longitude
    key = api_key
    forecast = forecastio.load_forecast(key, lat, lng).currently()
    print ("{} and {}º".format(forecast.summary, forecast.temperature))
    return "{} and {}º".format(forecast.summary, forecast.temperature)



