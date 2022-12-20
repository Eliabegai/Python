# Abra um audio em MP3 e reproduza ele.
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('music021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
