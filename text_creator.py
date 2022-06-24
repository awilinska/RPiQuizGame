import pygame
from variables import *

display = pygame.display.set_mode((width, height))

def textdraw(text, text_height, color, font_size):
    font = pygame.font.Font('/home/pi/Desktop/Play-Regular.ttf', font_size)
    text = font.render(text, True, color)
    text_rect = text.get_rect(center=(width//2, text_height))
    display.blit(text, text_rect)

def customtextdraw(text, position, color, font_size):
    font = pygame.font.SysFont('/home/pi/Desktop/Play-Regular.ttf', font_size)
    text = font.render(text, True, color)
    display.blit(text, position)
