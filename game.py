import pygame
from pygame.locals import *
from text_creator import *
import RPi.GPIO as GPIO
from ui import *
#from button_setup import *
import sys
import time

pygame.init()

start_screen = 1
main_menu = 2
controller_test = 3
details = 4
player_selection = 5
get_ready = 6
questions = 7
results = 8

button_time = time.time()
button_push = -1

p1_blue = 7
p1_green = 11
p1_yellow = 15
p1_red = 13

p2_blue = 29
p2_green = 31
p2_yellow = 33
p2_red = 35

p3_blue = 32
p3_green = 36
p3_yellow = 40
p3_red = 37

p4_blue = 12
p4_green = 16
p4_yellow = 18
p4_red = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(p1_blue, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p1_green, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p1_yellow, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p1_red, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(p2_blue, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p2_green, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p2_yellow, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p2_red, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(p3_blue, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p3_green, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p3_yellow, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p3_red, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(p4_blue, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p4_green, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p4_yellow, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p4_red, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_pushed(channel):
	global button_time
	global button_push
	time_now = time.time()
	if (time_now - button_time >= 0.3):
			button_push = channel
	button_time = time_now

GPIO.add_event_detect(p1_blue, GPIO.BOTH, callback=button_pushed)
GPIO.add_event_detect(p1_green, GPIO.BOTH, callback=button_pushed)
GPIO.add_event_detect(p1_yellow, GPIO.BOTH, callback=button_pushed)
GPIO.add_event_detect(p1_red, GPIO.BOTH, callback=button_pushed)

GPIO.add_event_detect(p2_blue, GPIO.BOTH, callback=button_pushed)
GPIO.add_event_detect(p2_green, GPIO.BOTH, callback=button_pushed)
GPIO.add_event_detect(p2_yellow, GPIO.BOTH, callback=button_pushed)
GPIO.add_event_detect(p2_red, GPIO.BOTH, callback=button_pushed)

GPIO.add_event_detect(p3_blue, GPIO.BOTH, callback=button_pushed)
GPIO.add_event_detect(p3_green, GPIO.BOTH, callback=button_pushed)
GPIO.add_event_detect(p3_yellow, GPIO.BOTH, callback=button_pushed)
GPIO.add_event_detect(p3_red, GPIO.BOTH, callback=button_pushed)

GPIO.add_event_detect(p4_blue, GPIO.BOTH, callback=button_pushed)
GPIO.add_event_detect(p4_green, GPIO.BOTH, callback=button_pushed)
GPIO.add_event_detect(p4_yellow, GPIO.BOTH, callback=button_pushed)
GPIO.add_event_detect(p4_red, GPIO.BOTH, callback=button_pushed)

display_now = start_screen

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

    # START SCREEN
    if (running == True) and (display_now == start_screen):
        
        display.fill(black)
        draw_title()

        clock = pygame.time.Clock()

        pygame.display.flip()

        loop = True

        while(loop):
            if (button_push == p1_blue):
                button_push = -1
                loop = False
                display_now = main_menu
                print("test1")

    # MAIN MENU
    if (running == True) and (display_now == main_menu):

        display.fill(black)
        draw_menu()

        pygame.display.flip()

        loop = True

        while(loop):
            if (button_push == p1_blue):
                button_push = -1
                loop = False
                display_now = player_selection

            if (button_push == p1_green):
                button_push = -1
                loop = False
                display_now = player_selection

            if (button_push == p1_yellow):
                button_push = -1
                loop = False
                display_now = controller_test

            if (button_push == p1_red):
                button_push = -1
                loop = False
                display_now = details

    #INFO
    if (running == True) and (display_now == details):

        display.fill(black)
        draw_info()
            
        pygame.display.flip()

        loop = True

        while (loop):
            if (button_push == p1_red):
                button_push = -1
                loop = False
                display_now = main_menu

    #TEST
    if (running == True) and (display_now == controller_test):

        display.fill(black)
        draw_test()
            
        pygame.display.flip()

        loop = True

        while(loop):
            # PLAYER 1
            if (button_push == p1_blue):
                button_push = -1
                loop = False
                p1_b = customtextdraw("niebieski", (200, height/2 - 180), blue, 25) 
            if (button_push == p1_green):
                button_push = -1
                loop = False
                p1_g = customtextdraw("zielony", (400, height/2 - 180), green, 25)
            if (button_push == p1_yellow):
                button_push = -1
                loop = False
                p1_y = customtextdraw("żółty", (600, height/2 - 180), yellow, 25)
            if (button_push == p1_red):
                button_push = -1
                loop = False
                p1_r = customtextdraw("czerwony", (800, height/2 - 180), red, 25)

            #PLAYER 2
            if (button_push == p2_blue):
                button_push = -1
                loop = False
                p2_b = customtextdraw("niebieski", (200, height/2 - 60), blue, 25)
            if (button_push == p2_green):
                button_push = -1
                loop = False
                p2_g = customtextdraw("zielony", (400, height/2 - 60), green, 25)
            if (button_push == p2_yellow):
                button_push = -1
                loop = False
                p2_y = customtextdraw("żółty", (600, height/2 - 60), yellow, 25)
            if (button_push == p2_red):
                button_push = -1
                loop = False
                p2_r = customtextdraw("czerwony", (800, height/2 - 60), red, 25)

            #PLAYER 3
            if (button_push == p3_blue):
                button_push = -1
                loop = False
                p3_b = customtextdraw("niebieski", (200, height/2 + 60), blue, 25)
            if (button_push == p3_green):
                button_push = -1
                loop = False
                p3_g = customtextdraw("zielony", (400, height/2 + 60), green, 25)
            if (button_push == p3_yellow):
                button_push = -1
                loop = False
                p3_y = customtextdraw("żółty", (600, height/2 + 60), yellow, 25)
            if (button_push == p3_red):
                button_push = -1
                loop = False
                p3_r = customtextdraw("czerwony", (800, height/2 + 60), red, 25)

            #PLAYER 4
            if (button_push == p4_blue):
                button_push = -1
                loop = False
                p4_b = customtextdraw("niebieski", (200, height/2 + 180), blue, 25)
            if (button_push == p4_green):
                button_push = -1
                loop = False
                p4_g = customtextdraw("zielony", (400, height/2 + 180), green, 25)
            if (button_push == p4_yellow):
                button_push = -1
                loop = False
                p4_y = customtextdraw("żółty", (600, height/2 + 180), yellow, 25)
            if (button_push == p4_red):
                button_push = -1
                loop = False
                p4_r = customtextdraw("czerwony", (800, height/2 + 180), red, 25)



pygame.quit()