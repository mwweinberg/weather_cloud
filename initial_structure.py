#Python 3.6

def relax():
    print("relaxing")

def start_storm():
    print("starting storm")

def in_storm():
    print("in the storm")

def end_storm():
    print("ending storm")

#starts things off in the clear
old_state = "clear"

#loops
while True:

    #asks for input that governs the behavior
    #this will eventually look for the tweet
    #and will probably be a function that looks at tweets
    state = input("> ")

    #if we are already in a storm (this is triggered by the else below)
    if old_state == "stormy":

        #"1" triggers the storm and keeps us in teh storm
        if state == "1":
            in_storm()
            old_state = "stormy"

        #if "1" isn't the input it is time to end the storm
        else:
            end_storm()
            old_state = "clear"

    #if things are clear
    else:

        #if the input is to start a storm
        if state == "1":
            #run the start storm element
            start_storm()
            #and change the setting to "in a storm"
            old_state = "stormy"

        #if it is calm and the goal is to stay calm...
        else:
            relax()
            old_state = "clear"
