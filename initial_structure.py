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
    return "clear"

def start_storm(id):
    print("starting storm " + id)
    filename = 'sounds/stormintro' + id + ".ogg"
    sounda = pygame.mixer.Sound(filename)
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    output_string = "stormy" + id
    return output_string

def in_storm(id_int):
    id = str(id_int)
    print("in the storm " + id)
    filename = 'sounds/stormmiddle' + id + '.ogg'
    sounda = pygame.mixer.Sound(filename)
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    output_string = "stormy" + id
    return output_string

def end_storm(id_int):
    id = str(id_int)
    print("ending storm " + id)
    filename = 'sounds/stormexit' + id + '.ogg'
    sounda = pygame.mixer.Sound(filename)
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    return "clear"



######################
#####Engine###########
######################


#starts things off in the clear
old_state = "clear"

#loops
while True:

    #asks for input that governs the behavior
    #this will eventually look for the tweet
    #and will probably be a function that looks at tweets
    #0 is calm, 1 is storm
    state = input("> ")


    ################################
    ###This section runs the storms#
    ################################
    #if we are already in a storm (this is triggered by the else below)
    if old_state == "stormy0":
        #"1" triggers the storm and keeps us in the storm
        if state == "1":
            old_state = in_storm(0)
        #if "1" isn't the input it is time to end the storm
        else:
            old_state = end_storm(0)

    elif old_state == "stormy1":
        if state == "1":
            old_state = in_storm(1)
        #if "1" isn't the input it is time to end the storm
        else:
            old_state = end_storm(1)

    elif old_state == "stormy2":
        if state == "1":
            old_state = in_storm(2)
        #if "1" isn't the input it is time to end the storm
        else:
            old_state = end_storm(2)

    #if things are clear
    #which is also the initial state
    else:
        #if the input is to start a storm
        if state == "1":
            #picks 0, 1, or 2
            picker = str(randint(0,2))
            old_state = start_storm(picker)

        #if it is calm and the goal is to stay calm...
        else:
            #clear()
            old_state = clear()
