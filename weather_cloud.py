#Python 3.6

from random import randint
import simpleaudio as sa


#open weather map client wrapper
import pyowm
import time

#for the db access
import sqlite3
import os

#imports the variables from the config.py file
from config import *

#create the data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

#identifies the db in the data directory
db = sqlite3.connect('data/weatherdb')
#creates the cursor
cursor = db.cursor()

#############################
#####Weather states##########
#############################

#these all ends with "return" and a state
#because that moves the changing of old_state into the
#function instead of putting it in the engine

def clear():
    #this is whatever relax is really going to do
    print("relaxing")
    #creates the audio object
    wave_obj = sa.WaveObject.from_wave_file("sounds/calm.wav")
    #plays the track
    play_obj = wave_obj.play()
    #waits until the track is done to move on
    #without this the script will immediately move on
    #after there are animations remove this
    #but unitl then if you don't have it the engine will immediately move on
    play_obj.wait_done()
    return 0

def start_storm(id):
    print("starting storm " + id)
    filename = 'sounds/stormintro' + id + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    #return output_string
    return id

def in_storm(id_int):
    id = str(id_int)
    print("in the storm " + id)
    filename = 'sounds/stormmiddle' + id + '.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    #return output_string
    return int(id)

def end_storm(id_int):
    id = str(id_int)
    print("ending storm " + id)
    filename = 'sounds/stormexit' + id + '.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    #return "clear"
    return 0

#############################
#####Weather data##########
#############################


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

    ##################################################
    ###This section queries the db and sets the state#
    ##################################################

    #TIME OFFSET FOR TARGET LOCATION IN SECONDS
    time_offset = 120

    #sets now rounded to zero decimal places
    now = int(time.time())

    #sets variable for time shifted target time (i.e. Tahiti time)
    target_time = now - time_offset

    #we're now looking for a hit in the db that will bump us out of the search

    #variable to see if there is a hit
    bumper = 0


    #queries the db looking for a match in adjusted time
    cursor.execute('''SELECT time_stamp, weather_code FROM users''')
    for row in cursor:
        #if there is an entry in the db that is +/- 20 seconds of target time
        if target_time - 20 < int(row[0]) < target_time + 20:
            #assign the corresponding code to the state
            state = str(weather_code_to_action(row[1]))
            print("weather code is " + str(row[1]) + " and state is " + str(state))
            print("adjusted time")
            #if there is a hit, bump out of this process and move to the action
            bumper = 1
        else:
            pass

    #if there hasn't been a hit in adjusted time, try for current time
    if bumper == 0:
        cursor.execute('''SELECT time_stamp, weather_code FROM users''')
        for row in cursor:
            if now - 20 < int(row[0]) < now + 20:
                state = str(weather_code_to_action(row[1]))
                print("weather code is " + str(row[1]) + " and state is " + str(state))
                print('current time')
                bumper = 1
        else:
            pass

    #if there is neither a hit on current time nor adjusted time, make it calm
    if bumper == 0:
        state = 0




    ################################
    ###This section runs the storms#
    ################################
    #if things are clear
    if old_state == 0:
        #if the input is to start a storm
        print("down here state is: " + str(state))
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
