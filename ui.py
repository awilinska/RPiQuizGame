import pygame
from text_creator import *
import random
from variables import *

def draw_menu():

    background = pygame.image.load(layout_menu).convert()
    display.blit(background, background_position)

    textdraw("DOMOTURNIEJ - DOMOWY TURNIEJ WIEDZY", 100, black, 45)

    textdraw("Tryb 1", 200, blue, 35)
    textdraw("Wszyscy gracze odpowiadają na wszystkie pytania", 230, gray, 15)

    textdraw("Tryb 2", 300, green, 35)
    textdraw("Gracze zgłaszają się do odpowiedzi na pytanie", 330, gray, 15)

    textdraw("Test kontrolerów", 400, yellow, 35)
    textdraw("Sprawdź działanie przycisków w kontrolerach", 430, gray, 15)

    textdraw("Informacje", 500, red, 35)
    textdraw("Informacje i źródła", 530, gray, 15)

    textdraw("Podpowiedź: używaj klawiszy o odpowiednich kolorach na kontrolerze GRACZA 1, by poruszać się po menu", 600, gray, 20)

def rand_line(fname):
    lines = open(fname, encoding='utf8').read().splitlines()
    return random.choice(lines)

def draw_info_mode1():
    background = pygame.image.load(layout_waiting).convert()
    display.blit(background, background_position)

    textdraw("Tryb 1", 200, black, 45)

    textdraw("Każdy z graczy odpowiada po kolei na pytanie.", 300, black, 30)
    textdraw("Numer gracza, który powinien udzielić odpowiedzi podświetla się na zielono.", 350, black, 30)
    textdraw("Po udzieleniu odpowiedz przez wszystkich graczy wyświetli się kolejne pytanie.", 400, black, 30)
    textdraw("Wygrywa gracz, który uzyskał największą liczbę punktów.", 450, black, 30)

def draw_info_mode2():
    background = pygame.image.load(layout_waiting).convert()
    display.blit(background, background_position)

    textdraw("Tryb 2", 200, black, 45)

    textdraw("Gracz zgłasza się do odpowiedzi na pytanie klikając niebieski przycisk.", 300, black, 30)
    textdraw("Numer gracza, który powinien udzielić odpowiedzi podświetla się na zielono.", 350, black, 30)
    textdraw("Po udzieleniu odpowiedz przez wybranego gracza wyświetli się kolejne pytanie.", 400, black, 30)
    textdraw("Wygrywa gracz, który uzyskał największą liczbę punktów.", 450, black, 30)

def draw_title():
    background = pygame.image.load(layout_start).convert()
    display.blit(background, background_position)

    textdraw("Domoturniej - domowy turniej wiedzy", height/2-100, black, 60)
    textdraw("START", height/2+70, blue, 30)
    textdraw("by Alicja Wilińska", height/2+200, gray, 15)
    textdraw("Podpowiedź: używaj klawiszy o odpowiednich kolorach na kontrolerze GRACZA 1, by poruszać się po menu", 600, gray, 20)

def draw_test():
    background = pygame.image.load(layout_waiting).convert()
    display.blit(background, background_position)

    textdraw("TEST KONTROLERÓW", height/2 - 280, black, 40)

    textdraw("Gracz 1", height/2 - 220, black, 30)
    customtextdraw("niebieski", (200, height/2 - 180), gray, 25)
    customtextdraw("zielony", (400, height/2 - 180), gray, 25)
    customtextdraw("żółty", (600, height/2 - 180), gray, 25)
    customtextdraw("czerwony", (800, height/2 - 180), gray, 25)

    textdraw("Gracz 2", height/2 - 100, black, 30)
    customtextdraw("niebieski", (200, height/2 - 60), gray, 25)
    customtextdraw("zielony", (400, height/2 - 60), gray, 25)
    customtextdraw("żółty", (600, height/2 - 60), gray, 25)
    customtextdraw("czerwony", (800, height/2 - 60), gray, 25)

    textdraw("Gracz 3", height/2 + 20, black, 30)
    customtextdraw("niebieski", (200, height/2 + 60), gray, 25)
    customtextdraw("zielony", (400, height/2 + 60), gray, 25)
    customtextdraw("żółty", (600, height/2 + 60), gray, 25)
    customtextdraw("czerwony", (800, height/2 + 60), gray, 25)

    textdraw("Gracz 4", height/2 + 140, black, 30)
    customtextdraw("niebieski", (200, height/2 + 180), gray, 25)
    customtextdraw("zielony", (400, height/2 + 180), gray, 25)
    customtextdraw("żółty", (600, height/2 + 180), gray, 25)
    customtextdraw("czerwony", (800, height/2 + 180), gray, 25)

    textdraw("Test zamknie się automatycznie w ciągu 5 sekund od wciśnięcia ostatniego przycisku.", height/2 + 280, gray, 20)

def draw_info():
    background = pygame.image.load(layout_details).convert()
    display.blit(background, background_position)

    textdraw("Autor: Alicja Wilińska", height/2, black, 30)
    textdraw("Gra wykonana w ramach pracy inżynierskiej.", height/2+70, black, 30)
    
    textdraw("Powrót", height/2+200, red, 15)
    
def draw_quenum():

    background = pygame.image.load(layout_menu).convert()
    display.blit(background, background_position)

    textdraw("Wybierz ilość pytań", 100, black, 45)
    
    textdraw("10", 200, blue, 35)
    textdraw("Szybka rozgrywka", 230, gray, 15)
    
    textdraw("25", 300, green, 35)
    textdraw("Standardowe wyzwanie", 330, gray, 15)
    
    textdraw("50", 400, yellow, 35)
    textdraw("Maraton pełen wiedzy", 430, gray, 15)
    
    textdraw("powrót do menu", 520, red, 35)
