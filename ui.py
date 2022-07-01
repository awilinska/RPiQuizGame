import pygame
from text_creator import *
import random
from variables import *

def draw_menu():

    background = pygame.image.load(layout_menu).convert()
    display.blit(background, background_position)

    textdraw("DOMOTURNIEJ - DOMOWY TURNIEJ WIEDZY", 100, black, 45)

    textdraw("Gra", 200, blue, 35)
    textdraw("Zmierzcie się w jednym z dwóch trybów gry", 230, gray, 15)

    textdraw("Test kontrolerów", 300, green, 35)
    textdraw("Sprawdź działanie przycisków w kontrolerach", 330, gray, 15)

    textdraw("Informacje", 400, yellow, 35)
    textdraw("Informacje i źródła", 430, gray, 15)

    textdraw("Wyjdź", 505, red, 35)
    textdraw("Wyjście z gry", 535, gray, 15)

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
    textdraw("START", height/2+40, blue, 30)
    textdraw("WYJDŹ", height/2+130, red, 30)
    textdraw("by Alicja Wilińska", height/2+200, gray, 15)
    textdraw("Podpowiedź: używaj klawiszy o odpowiednich kolorach na kontrolerze GRACZA 1, by poruszać się po menu", 600, gray, 20)

def draw_test():
    background = pygame.image.load(layout_waiting).convert()
    display.blit(background, background_position)

    textdraw("TEST KONTROLERÓW", height/2 - 250, black, 40)

    customtextdraw("Gracz 1", (300,200), black, 30)
    customtextdraw("Gracz 2", (700,200), black, 30)
    customtextdraw("Gracz 3", (300,400), black, 30)
    customtextdraw("Gracz 4", (700,400), black, 30)

    textdraw("Test zamknie się automatycznie w ciągu 15 sekund od uruchomienia.", height/2 + 280, gray, 20)

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

def draw_modes():
    background = pygame.image.load(layout_modes).convert()
    display.blit(background, background_position)

    textdraw("Wybierz tryb gry", 100, black, 45)
    
    textdraw("Wiedza", 275, blue, 35)
    textdraw("Wszyscy gracze odpowiadają na wszystkie pytania", 305, gray, 15)

    textdraw("Refleks", 375, green, 35)
    textdraw("Gracze zgłaszają się do odpowiedzi na pytanie", 405, gray, 15)
    
    textdraw("powrót do menu", 485, red, 20)
