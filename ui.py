import pygame
from text_creator import *
import random
from variables import *

def draw_menu():

    background = pygame.image.load(layout_menu).convert()
    display.blit(background, background_position)

    textdraw("HOMEPETITON - KNOWLEDGE COMPETITION!", 100, black, 45)

    textdraw("Play", 200, blue, 35)
    textdraw("Face each other in one of two game modes", 230, gray, 15)

    textdraw("Controller test", 300, green, 35)
    textdraw("Check operation of buttons on controllers", 330, gray, 15)

    textdraw("Details", 400, yellow, 35)
    textdraw("Details and credits", 430, gray, 15)

    textdraw("Quit", 505, red, 35)
    textdraw("Quit the game", 535, gray, 15)

    textdraw("Hint: use the keys with the corresponding colors on PLAYER 1's controller to navigate the menu", 600, gray, 20)

def rand_line(fname):
    lines = open(fname, encoding='utf8').read().splitlines()
    return random.choice(lines)

def draw_info_mode1():
    background = pygame.image.load(layout_waiting).convert()
    display.blit(background, background_position)

    textdraw("Knowledge", 200, black, 45)

    textdraw("Each player answers the question in turn.", 300, black, 30)
    textdraw("The number of the player who should give the answer is highlighted in green.", 350, black, 30)
    textdraw("After all players have answered, another question will be displayed.", 400, black, 30)
    textdraw("The player with the highest number of points wins.", 450, black, 30)

def draw_info_mode2():
    background = pygame.image.load(layout_waiting).convert()
    display.blit(background, background_position)

    textdraw("Speed", 200, black, 45)

    textdraw("The player volunteers to answer the question by clicking the blue button.", 300, black, 30)
    textdraw("The number of the player who should give the answer is highlighted in green.", 350, black, 30)
    textdraw("After the selected player answers, another question will be displayed.", 400, black, 30)
    textdraw("The player with the highest number of points wins.", 450, black, 30)

def draw_title():
    background = pygame.image.load(layout_start).convert()
    display.blit(background, background_position)

    textdraw("HOMEPETITON - KNOWLEDGE COMPETITION!", height/2-100, black, 60)
    textdraw("START", height/2+40, blue, 30)
    textdraw("QUIT", height/2+130, red, 30)
    textdraw("by Alicja Wilińska", height/2+200, gray, 15)
    textdraw("Hint: use the keys with the corresponding colors on PLAYER 1's controller to navigate the menu", 600, gray, 20)

def draw_test():
    background = pygame.image.load(layout_waiting).convert()
    display.blit(background, background_position)

    textdraw("CONTROLLER TEST", height/2 - 250, black, 40)

    customtextdraw("Player 1", (300,200), black, 30)
    customtextdraw("Player 2", (700,200), black, 30)
    customtextdraw("Player 3", (300,400), black, 30)
    customtextdraw("Player 4", (700,400), black, 30)

    textdraw("The test will automatically close within 15 seconds of startup.", height/2 + 280, gray, 20)

def draw_info():
    background = pygame.image.load(layout_details).convert()
    display.blit(background, background_position)

    textdraw("Autor: Alicja Wilińska", height/2, black, 30)
    textdraw("This project is being developed as part of a thesis at the West Pomeranian Business School (Stettin).", height/2+70, black, 30)
    
    textdraw("Back", height/2+200, red, 15)
    
def draw_quenum():

    background = pygame.image.load(layout_menu).convert()
    display.blit(background, background_position)

    textdraw("Choose the number of questions", 100, black, 45)
    
    textdraw("10", 200, blue, 35)
    textdraw("Quick game", 230, gray, 15)
    
    textdraw("25", 300, green, 35)
    textdraw("Standard challenge", 330, gray, 15)
    
    textdraw("50", 400, yellow, 35)
    textdraw("A marathon full of knowledge", 430, gray, 15)
    
    textdraw("back to menu", 520, red, 35)

def draw_modes():
    background = pygame.image.load(layout_modes).convert()
    display.blit(background, background_position)

    textdraw("Select a game mode", 100, black, 45)
    
    textdraw("Knowledge", 275, blue, 35)
    textdraw("All players answer all questions", 305, gray, 15)

    textdraw("Speed", 375, green, 35)
    textdraw("Players come forward to answer the question", 405, gray, 15)
    
    textdraw("back to menu", 485, red, 20)
