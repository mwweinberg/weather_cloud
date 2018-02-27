#python3

#target API endpoint
#http://api.openweathermap.org/data/2.5/weather?id=[locationID]&appid=[API KEY]

#pyowm documentation:
#https://github.com/csparpa/pyowm

#weather code list:
#https://openweathermap.org/weather-conditions

#open weather map client wrapper
import pyowm

#imports the variables from the config.py file
from config import *

locationID = '4033936'

print('http://api.openweathermap.org/data/2.5/weather?id='+locationID+'&appid='+API_KEY)

owm = pyowm.OWM(API_KEY)

observation = owm.weather_at_id(4033936)

w = observation.get_weather()
print(w)

wind = w.get_wind()
wind_speed = wind['speed']

print(wind_speed)

id = w.get_weather_code()
print(id)
