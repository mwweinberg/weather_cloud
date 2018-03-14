#for the db access
import sqlite3
import os
import time

#create the data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

#identifies the db in the data directory
db = sqlite3.connect('data/weatherdb')
#creates the cursor
cursor = db.cursor()


now_stamp = int(time.time())
db_cutoff = now_stamp - 180

#queries the db
cursor.execute('''SELECT time_stamp, weather_code FROM users''')
for row in cursor:
    #matches the time_stam to a condition
    if db_cutoff < int(row[0]) < (db_cutoff+120):
        #and if it is a hit prints the weather code
        print(row[1])
