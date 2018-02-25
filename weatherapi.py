#python3

#target API endpoint
#http://api.openweathermap.org/data/2.5/weather?id=[API KEY]

#pyowm documentation:
#https://github.com/csparpa/pyowm

#open weather map client wrapper
import pyowm

#imports the variables from the config.py file
from config import *

owm = pyowm.OWM(API_KEY)

observation = owm.weather_at_id(4033936)

w = observation.get_weather()
print(w)

print(w.get_wind())
