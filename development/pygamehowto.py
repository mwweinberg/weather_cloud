import pygame

# setup mixer to avoid sound lag
pygame.mixer.pre_init(44100, -16, 2, 2048)
#initialize pygame
pygame.mixer.init()

#load the sound file
sounda = pygame.mixer.Sound('sounds/241913/calm1.ogg')
#play the sound file
sounda.play()
#not sure what this does but without it  you can't hear the sound
channela = sounda.play()
while channela.get_busy():
   pygame.time.delay(100)
