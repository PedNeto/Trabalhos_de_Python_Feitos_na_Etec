import pygame
import time

def som():
    pygame.mixer.init()
    pygame.mixer.music.load('E:/Aula_Programação_e_ Algoritimo_Edson/teste.mp3')
    pygame.mixer.music.play()
    time.sleep(7)

som()