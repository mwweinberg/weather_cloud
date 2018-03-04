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

def in_storm(id):
    print("in the storm " + id)
    filename = 'sounds/stormmidle' + id + '.ogg'
    sounda = pygame.mixer.Sound(filename)
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    output_string = "stormy" + id
    return output_string

def end_storm(id):
    print("ending storm " + id)
    filename = 'sounds/stormexit' + id + '.ogg'
    sounda = pygame.mixer.Sound(filename)
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    return "clear"





def start_storm0():
    print("starting storm0")

    sounda = pygame.mixer.Sound('sounds/59028/storm0intro.ogg')
    sounda.play()
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    return "stormy0"


def in_storm0():
    print("in the storm0")

    sounda = pygame.mixer.Sound('sounds/59028/storm0middle.ogg')
    sounda.play()
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    return "stormy0"


def end_storm0():
    print("ending storm0")

    sounda = pygame.mixer.Sound('sounds/59028/storm0exit.ogg')
    sounda.play()
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    return "clear"


def start_storm1():
    print("starting storm1")

    sounda = pygame.mixer.Sound('sounds/54205/storm1intro.ogg')
    sounda.play()
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    return "stormy1"


def in_storm1():
    print("in the storm1")

    sounda = pygame.mixer.Sound('sounds/54205/storm1middle.ogg')
    sounda.play()
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    return "stormy1"


def end_storm1():
    print("ending storm1")

    sounda = pygame.mixer.Sound('sounds/54205/storm1exit.ogg')
    sounda.play()
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    return "clear"


def start_storm2():
    print("starting storm2")

    sounda = pygame.mixer.Sound('sounds/278865/storm2intro.ogg')
    sounda.play()
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    return "stormy2"


def in_storm2():
    print("in the storm2")

    sounda = pygame.mixer.Sound('sounds/278865/storm2middle.ogg')
    sounda.play()
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    return "stormy2"


def end_storm2():
    print("ending storm2")

    sounda = pygame.mixer.Sound('sounds/278865/storm2exit.ogg')
    sounda.play()
    channela = sounda.play()
    while channela.get_busy():
       pygame.time.delay(100)
    return "stormy2"


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
            #run the storm0
            in_storm0()
            #in_storm0 is called with old_state = in_storm0()
            #because that allows the end of in_storm0
            #to return the correct old_state
            old_state = "stormy0"
        #if "1" isn't the input it is time to end the storm
        else:
            end_storm0()
            old_state = "clear"

    elif old_state == "stormy1":
        if state == "1":
            in_storm1()
            old_state = "stormy1"
        else:
            end_storm1()
            old_state = "clear"

    elif old_state == "stormy2":
        if state == "1":
            in_storm2()
            old_state = "stormy2"
        else:
            end_storm2()
            old_state = "clear"

    #if things are clear
    #which is also the initial state
    else:
        #if the input is to start a storm
        if state == "1":
            #picks 0, 1, or 2
            picker = randint(0,2)
            #if picker is 0 run storm0
            if picker == 0:
                #run the start storm element
                start_storm0()
                #indicate that we are in a storm state
                old_state = "stormy0"

            elif picker == 1:
                start_storm1()
                old_state = "stormy1"

            elif picker == 2:
                start_storm2()
                old_state = "stormy2"

            else:
                print("error in the randomly assign storm section")

        #if it is calm and the goal is to stay calm...
        else:
            clear()
            old_state = "clear"
