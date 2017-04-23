#Python 3.6

from random import randint
import pygame

# setup mixer to avoid sound lag
pygame.mixer.pre_init(44100, -16, 2, 2048)
#initialize pygame
pygame.mixer.init()

#############################
#####Weather states##########
#############################

#these all ends with "return" and a state
#because that moves the changing of old_state into the
#function instead of putting it in the engine

def relax():
    #this is whatever relax is really going to do
    print("relaxing")
    #load the sound file
    sounda = pygame.mixer.Sound('sounds/241913/calm1.ogg')
    #play the sound file
    sounda.play()
    #not sure what this does but without it  you can't hear the sound
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)

    #and this sets the old_state properly in the engine
    return "clear"

def start_storm1():
    print("starting storm1")
    return "stormy1"
def in_storm1():
    print("in the storm1")
    return "stormy1"
def end_storm1():
    print("ending storm1")
    return "clear"

def start_storm2():
    print("starting storm2")
    return "stormy2"
def in_storm2():
    print("in the storm2")
    return "stormy2"
def end_storm2():
    print("ending storm2")
    return "clear"

def start_storm3():
    print("starting storm3")
    return "stormy3"
def in_storm3():
    print("in the storm3")
    return "stormy3"
def end_storm3():
    print("ending storm3")
    return "clear"





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
        #"1" triggers the storm and keeps us in the storm
        if state == "1":
            #in_storm1 is called with old_state = in_storm1()
            #because that allows the end of in_storm1
            #to return the correct old_state
            old_state = in_storm1()
        #if "1" isn't the input it is time to end the storm
        else:
            old_state = end_storm1()

    elif old_state == "stormy2":
        if state == "2":
            old_state = in_storm2()
        else:
            old_state = end_storm2()

    elif old_state == "stormy3":
        if state == "1":
            old_state = in_storm3()
        else:
            old_state = end_storm3()

    #if things are clear
    #which is also the initial state
    else:
        #if the input is to start a storm
        if state == "1":
            #picks 0 or 1
            picker = randint(0,1)
            #if picker is 0 run storm1
            if picker == 0:
                #run the start storm element
                old_state = start_storm1()

            elif picker == 1:
                old_state = start_storm3()

            else:
                print("error in the randomly assign storm section")
        elif state == "2":
            old_state = start_storm2()

        #if it is calm and the goal is to stay calm...
        else:
            old_state = relax()
