import pygame

black = (0, 0, 0)
gray = (127, 127, 127)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

width = 1100
height = 700

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
