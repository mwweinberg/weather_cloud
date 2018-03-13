# weather_cloud
A cloud that simulates weather in Tahiti when positioned on the US east coast.  In order to correct for the time difference, it will build a db of weather conditions in Tahiti when it starts.  It will rely on "current" conditions (i.e. whatever is happening at that moment on the ground) until that db has enough data to allow it to rely on 'current adjusted' conditions (i.e. if it is 4pm in NY, what happened at 4pm in Tahiti).

The primary scripts will be weatherdb.py to create the weather database and weather_cloud.py to respond. The rest of the scripts (mostly in the development folder) were for learning how various bits worked.  

Eventually this will have a raspberry pi triggering sound and lights to simulate the weather conditions.


