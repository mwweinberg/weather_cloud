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

#this is just for testing to print out the URL it is hitting and can be removed
locationID = '4033936'
print('http://api.openweathermap.org/data/2.5/weather?id='+locationID+'&appid='+API_KEY)

def get_weather_code():

    #sets up the weather object
    owm = pyowm.OWM(API_KEY)
    observation = owm.weather_at_id(4033936)
    w = observation.get_weather()

    #gets the current weather code
    weather_code = w.get_weather_code()
    #for debugging
    print(weather_code)

    #looks for calm codes
    if weather_code == 701 or 801 or 802 or 803 or 951 or 952 or 953 or 954 or 955:
        print('calm state')
        return 0
    else:
        print('storm_state')
        return 1

get_weather_code()
print(get_weather_code())
