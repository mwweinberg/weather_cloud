import sqlite3
import os

#open weather map client wrapper
import pyowm
import time

#imports the variables from the config.py file
from config import *

#create the data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

#create the db in the data directory 
db = sqlite3.connect('data/weatherdb')

# Get a cursor object and create the table
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(time_stamp INTEGER,
                       weather_code INTEGER)
''')
db.commit()

#defines the weather object
owm = pyowm.OWM(API_KEY)

while True:

    #pulls a time stamp
    now_stamp = int(time.time())
    #print("now_stamp = " + str(now_stamp))

    #pulls the weather data
    observation = owm.weather_at_id(4033936)
    w = observation.get_weather()
    condition = int(w.get_weather_code())
    #print("condition = " + str(condition))

    #writes the time stamp and weather data into the db
    cursor.execute('''INSERT INTO users(time_stamp, weather_code)
                      VALUES(?,?)''', (now_stamp,condition))
    print("now_stamp = " + str(now_stamp) + " condition = " + str(condition) + " to db")
    db.commit()

    #sets the database cutoff at everyting more than 3 minutes old
    db_cutoff = now_stamp - 180
    print("db_cutoff = " + str(db_cutoff))

    #removes the old entries
    #and yes that comma afer db_cutoff is necessary
    cursor.execute('''DELETE FROM users WHERE time_stamp < ? ''', (db_cutoff,))
    db.commit()


    time.sleep(10)
