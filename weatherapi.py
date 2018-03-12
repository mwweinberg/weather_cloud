#python3

#target API endpoint
#http://api.openweathermap.org/data/2.5/weather?id=[API KEY]

#pyowm documentation:
#https://github.com/csparpa/pyowm

#open weather map client wrapper
import pyowm
import time

#imports the variables from the config.py file
from config import *

#defines the weather object
owm = pyowm.OWM(API_KEY)

condition_dict = {}

while True:
    #pulls the weather data
    observation = owm.weather_at_id(4033936)

    w = observation.get_weather()
    condition = int(w.get_weather_code())

    print(condition)

    #dictionary with current time (rounded to second) and condition
    now_stamp = int(time.time())
    condition_dict[now_stamp] = condition
    print(condition_dict)

    #looks for a key that is ~2 minutes ago
    #this will be the function used to find the action match when
    #it is integrated into the larger script
    for i in condition_dict:
        #if the key is within two minutes of now (+/- 20 seconds)
        if (i + 100) <= now_stamp <= (i + 140):
            #print this
            print("Two minutes ago the condition was: " + str(condition_dict[i]))

    #temporary dict becuase you can't delete things in a dict duringa loop
    #this will be the function used to cap the size of the dictionary
    #once it is integrated into the larger script
    cleaning_dict = {}
    #tries to clean up old keys
    for i in condition_dict:
        #if i is less than 240 seconds old
        if now_stamp < (i + 240):
            #add it to the temporary dictionary
            cleaning_dict[i] = condition_dict[i]

    #once the capped temp dict has been created swap it in for the old one
    condition_dict = cleaning_dict


    time.sleep(30)
