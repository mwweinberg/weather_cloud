#Python 3.6

from random import randint
import pygame

# setup mixer to avoid sound lag
pygame.mixer.pre_init(44100, -16, 2, 2048)
#initialize pygame
pygame.mixer.init()

#open weather map client wrapper
import pyowm
import time

#imports the variables from the config.py file
from config import *

#defines the weather object
owm = pyowm.OWM(API_KEY)

#dictionary to hold the weather conditions
condition_dict = {}

#holds the time that the latest reading was taken
sample_time = 0

#############################
#####Weather states##########
#############################

#these all ends with "return" and a state
#because that moves the changing of old_state into the
#function instead of putting it in the engine

def clear():
    #this is whatever relax is really going to do
    print("relaxing")
    #load the sound file
    sounda = pygame.mixer.Sound('sounds/calm.ogg')
    #play the sound file
    sounda.play()
    #not sure what this does but without it  you can't hear the sound
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    #sets the storm state
    #do this here because resetting the storm state alwas happens
    return 0

def start_storm(id):
    print("starting storm " + id)
    filename = 'sounds/stormintro' + id + ".ogg"
    sounda = pygame.mixer.Sound(filename)
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    output_string = "stormy" + id
    #return output_string
    return id

def in_storm(id_int):
    id = str(id_int)
    print("in the storm " + id)
    filename = 'sounds/stormmiddle' + id + '.ogg'
    sounda = pygame.mixer.Sound(filename)
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    output_string = "stormy" + id
    #return output_string
    return int(id)

def end_storm(id_int):
    id = str(id_int)
    print("ending storm " + id)
    filename = 'sounds/stormexit' + id + '.ogg'
    sounda = pygame.mixer.Sound(filename)
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    #return "clear"
    return 0

#############################
#####Weather data##########
#############################

#obtains the weather data and adds it to the dictionary
def get_weather():
    #pulls the weather data
    observation = owm.weather_at_id(4033936)

    #gets the current weather code
    w = observation.get_weather()
    condition = int(w.get_weather_code())

    #dictionary with current time (rounded to second) and condition
    now_stamp = int(time.time())
    condition_dict[now_stamp] = condition

    return now_stamp

#finds the weather code for a moment
#can call with find_weather(int(time.time())
def find_weather(action_time):
    #looks for a key that is ~2 minutes ago
    #this will be the function used to find the action match when
    #it is integrated into the larger script
    for i in condition_dict:
        #if the key is within two minutes of now (+/- 20 seconds)
        # set this for the number of seconds back in time you want to look for
        if (i + 100) <= action_time <= (i + 140):
            #print this
            print("Two minutes ago the condition was: " + str(condition_dict[i]))
            return condition_dict[i]
        #if it can't find one that is old enough it will just use one close to action_time
        elif (i - 20) <= action_time <= (i + 20):
            print("Right now the condition is: " + str(condition_dict[i]))
            return condition_dict[i]
        else:
            print("there is no time match")
            return 800

#caps the size of the dictionary
def cap_dictionary():
    #temporary dict becuase you can't delete things in a dict duringa loop
    #this will be the function used to cap the size of the dictionary
    #once it is integrated into the larger script
    cleaning_dict = {}
    #tries to clean up old keys
    for i in condition_dict:
        #if i is less than 240 seconds old
        if sample_time < (i + 240):
            #add it to the temporary dictionary
            cleaning_dict[i] = condition_dict[i]

    #once the capped temp dict has been created swap it in for the old one
    return cleaning_dict



#turns the weather code into an action for the engine
#probably call with 'weather_code_to_action(find_weather(int(time.time())'
#codes are https://openweathermap.org/weather-conditions
def weather_code_to_action(code):
    #basically calm
    if code in (300, 301, 701, 741, 800, 801, 802, 803, 904, 951, 952, 953, 954):
        return 0
    #if it is not calm it is storming
    else:
        return 1






######################
#####Engine###########
######################


#starts things off in the clear
old_state = 0

#loops
while True:

    #gets the relevant weather condition on the ground
    #all print statements are for troubleshooting
    sample_time = get_weather()
    time_var = int(time.time())
    print("time_var = " + str(time_var))
    fw = find_weather(time_var)
    print("fw = " + str(fw))
    state = str(weather_code_to_action(fw))
    print("state = " + state)
    print("-----------")

    #cleans up the dictionary 
    condition_dict = cap_dictionary()
    print(condition_dict)




    ################################
    ###This section runs the storms#
    ################################
    #if things are clear
    if old_state == 0:
        #if the input is to start a storm
        if state == "1":
            #picks 1, 2, or 3
            picker = str(randint(1,3))
            old_state = start_storm(picker)

        #if it is calm and the goal is to stay calm...
        else:
            #clear()
            old_state = clear()
    #if we are in a storm
    elif int(old_state) > 0:
        #and we want to continue the storm
        if int(state) == 1:
            old_state = in_storm(old_state)
        #or we want to wrap the storm up
        else:
            old_state = end_storm(old_state)
    else:
        print("Error in the storms")
