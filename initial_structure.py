#Python 3.6

def relax():
    print("relaxing")

def start_storm1():
    print("starting storm1")

def in_storm1():
    print("in the storm1")

def end_storm1():
    print("ending storm1")

def start_storm2():
    print("starting storm2")

def in_storm2():
    print("in the storm2")

def end_storm2():
    print("ending storm2")

#starts things off in the clear
old_state = "clear"

#loops
while True:

    #asks for input that governs the behavior
    #this will eventually look for the tweet
    #and will probably be a function that looks at tweets
    state = input("> ")

    #if we are already in a storm (this is triggered by the else below)
    if old_state == "stormy1":

        #"1" triggers the storm and keeps us in teh storm
        if state == "1":
            in_storm1()
            old_state = "stormy1"

        #if "1" isn't the input it is time to end the storm
        else:
            end_storm1()
            old_state = "clear"

    elif old_state == "stormy2":

        if state == "2":
            in_storm2()
            old_state = "stormy2"

        else:
            end_storm2()
            old_state = "clear"

    #if things are clear
    else:

        #if the input is to start a storm
        if state == "1":
            #run the start storm element
            start_storm1()
            #and change the setting to "in a storm"
            old_state = "stormy1"

        elif state == "2":
            start_storm2()
            old_state = "stormy2"

        #if it is calm and the goal is to stay calm...
        else:
            relax()
            old_state = "clear"
