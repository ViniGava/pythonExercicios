"""Desenvolva um programe que toque um áudio mp3"""

import pygame

print('\033[1;31m-=-\033[m'*30)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
pygame.quit()
print('\033[1;31m-=-\033[m'*30)
