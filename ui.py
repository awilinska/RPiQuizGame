import pygame
from text_creator import *
import random

background_position = [0,0]

def draw_menu():

    background = pygame.image.load("/home/pi/Desktop/layout-menu.png").convert()
    display.blit(background, background_position)


    title = textdraw("DOMOTURNIEJ - DOMOWY TURNIEJ WIEDZY", 100, black, 45)
    mode1 = textdraw("Tryb 1", 200, blue, 35)
    mode1_info = textdraw("Wszyscy gracze odpowiadają na wszystkie pytania", 230, gray, 15)
    mode2 = textdraw("Tryb 2", 300, green, 35)
    mode2_info = textdraw("Gracze zgłaszają się do odpowiedzi na pytanie", 330, gray, 15)
    control_test = textdraw("Test kontrolerów", 400, yellow, 35)
    control_test_info = textdraw("Sprawdź działanie przycisków w kontrolerach", 430, gray, 15)
    about = textdraw("Informacje", 500, red, 35)
    about_info = textdraw("Informacje i źródła", 530, gray, 15)
    hint = textdraw("Podpowiedź: używaj klawiszy o odpowiednich kolorach, by poruszać się po menu", 600, gray, 20)

def rand_line(fname):
    lines = open(fname, encoding='utf8').read().splitlines()
    return random.choice(lines)

# def draw_question():
#     global correct

#     line = rand_line("/home/pi/Desktop/QUESTIONS.txt")
#     detail = line.split(",")

#     question = textdraw((detail[0]), 100, white, 45)
#     a = textdraw((detail[1]), 200, blue, 35)
#     b = textdraw((detail[2]), 300, green, 35)
#     c = textdraw((detail[3]), 400, yellow, 35)
#     d = textdraw((detail[4]), 500, red, 35)

#     ready = customtextdraw("Gotowi:", (50,550), white, 25)
#     player1 = customtextdraw("Gracz 1", (200,600), white, 25)
#     player2 = customtextdraw("Gracz 2", (400,600), gray, 25)
#     player3 = customtextdraw("Gracz 3", (600,600), white, 25)
#     player4 = customtextdraw("Gracz 4", (800,600), gray, 25)

#     correct = detail[5]

#     pygame.draw.circle(display, magenta, (1000,600), 50, 0)

#     timer = customtextdraw("15", (975,570), black, 40)

# def draw_results():
#     results = textdraw("Wyniki", 100, white, 45)

#     first = textdraw("1. Gracz 3    50 pkt", 250, yellow, 45)
#     second = textdraw("2. Gracz 1   30 pkt", 350, magenta, 45)
#     third = textdraw("3. Gracz 4    20 pkt", 450, magenta, 45)
#     fourth = textdraw("4. Gracz 2   10 pkt", 550, magenta, 45)

#     quit = textdraw("powrót do menu", 650, red, 25)

def draw_getready():
    time = 10

    get_ready = textdraw("Przygotujcie się", height/2, white, 60)
    timer = textdraw(("Gra rozpocznie się za " + str(time)), height/2+70, white, 30)

def draw_players():
    button = textdraw("Kliknij niebieski przycisk na kontrolerze", 100, white, 45)
    button_info = textdraw("Gracz, który nie aktywuje kontrolera w ciągu 15 sekund nie weźmie udziału w grze", 150, gray, 15)

    player1 = textdraw("Gracz 1", 250, gray, 45)
    player2 = textdraw("Gracz 2", 350, green, 45)
    player3 = textdraw("Gracz 3", 450, green, 45)
    player4 = textdraw("Gracz 4", 550, gray, 45)

    pygame.draw.circle(display, red, (1000,600), 50, 0)
    timer = customtextdraw("15", (975,570), black, 40)

def draw_title():
    background = pygame.image.load("/home/pi/Desktop/start-layout.png").convert()
    display.blit(background, background_position)

    title = textdraw("Domoturniej - domowy turniej wiedzy", height/2-100, black, 60)
    start = textdraw("START", height/2+70, blue, 30)
    author = textdraw("by Alicja Wilińska", height/2+200, gray, 15)
    hint = textdraw("Podpowiedź: używaj klawiszy o odpowiednich kolorach, by poruszać się po menu", 600, gray, 20)

def draw_test():

    title = textdraw("TEST KONTROLERÓW", height/2 - 280, white, 40)

    p1 = textdraw("Gracz 1", height/2 - 200, white, 30)
    p1_b = customtextdraw("niebieski", (200, height/2 - 180), white, 25)
    p1_g = customtextdraw("zielony", (400, height/2 - 180), white, 25)
    p1_y = customtextdraw("żółty", (600, height/2 - 180), white, 25)
    p1_r = customtextdraw("czerwony", (800, height/2 - 180), white, 25)

    p2 = textdraw("Gracz 2", height/2 - 80, white, 30)
    p2_b = customtextdraw("niebieski", (200, height/2 - 60), white, 25)
    p2_g = customtextdraw("zielony", (400, height/2 - 60), white, 25)
    p2_y = customtextdraw("żółty", (600, height/2 - 60), white, 25)
    p2_r = customtextdraw("czerwony", (800, height/2 - 60), white, 25)

    p3 = textdraw("Gracz 3", height/2 + 40, white, 30)
    p3_b = customtextdraw("niebieski", (200, height/2 + 60), white, 25)
    p3_g = customtextdraw("zielony", (400, height/2 + 60), white, 25)
    p3_y = customtextdraw("żółty", (600, height/2 + 60), white, 25)
    p3_r = customtextdraw("czerwony", (800, height/2 + 60), white, 25)

    p4 = textdraw("Gracz 4", height/2 + 160, white, 30)
    p4_b = customtextdraw("niebieski", (200, height/2 + 180), white, 25)
    p4_g = customtextdraw("zielony", (400, height/2 + 180), white, 25)
    p4_y = customtextdraw("żółty", (600, height/2 + 180), white, 25)
    p4_r = customtextdraw("czerwony", (800, height/2 + 180), white, 25)

    back = textdraw("powrót", height/2 + 280, red, 20)

def draw_info():
    background = pygame.image.load("/home/pi/Desktop/details-layout.png").convert()
    display.blit(background, background_position)

    author = textdraw("Autor: Alicja Wilińska", height/2, black, 30)
    info = textdraw("Gra wykonana w ramach pracy inżynierskiej.", height/2+70, black, 30)
    back = textdraw("Powrót", height/2+200, red, 15)


