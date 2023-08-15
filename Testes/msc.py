import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('msc1.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
o=str(input())
if o=='s':
    pygame.mixer.music.pause()