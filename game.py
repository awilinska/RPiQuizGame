import pygame
from pygame.locals import *
from pygame import mixer
from text_creator import *
import RPi.GPIO as GPIO
from ui import *
import sys
import time
import random

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

start_screen = 1
main_menu = 2
controller_test = 3
details = 4
player_selection = 5
get_ready = 6
questions = 7
results = 8
mode1 = 9
mode2 = 0
info_mode1 = 10
info_mode2 = 11
quenum_1 = 12
quenum_2 = 13

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
                display_now = quenum_1

            if (button_push == p1_green):
                button_push = -1
                loop = False
                display_now = quenum_2

            if (button_push == p1_yellow):
                button_push = -1
                loop = False
                display_now = controller_test

            if (button_push == p1_red):
                button_push = -1
                loop = False
                display_now = details

    # INFO
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

    # TEST
    if (running == True) and (display_now == controller_test):

        display.fill(black)
        draw_test()
            
        pygame.display.flip()

        timer_start = time.time()
        timer_stop = 5

        loop = True

        while(loop):

            timer = time.time() - timer_start

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
                p4_r = customtextdraw("czerwony", (800, height/2 + 180), red, 25)

            if timer > timer_stop:
                loop = False
                display_now = main_menu

    #QUESTIONS NUMBER MODE 1
    if (running == True) and (display_now == quenum_1):

        display.fill(black)
        draw_quenum()
        pygame.display.flip()

        loop = True
        
        while(loop):
            if (button_push == p1_blue):
                button_push = -1
                loop = False
                quenum = int(10)
                display_now = info_mode1

            if (button_push == p1_green):
                button_push = -1
                loop = False
                quenum = int(25)
                display_now = info_mode1

            if (button_push == p1_yellow):
                button_push = -1
                loop = False
                quenum = int(50)
                display_now = info_mode1

            if (button_push == p1_red):
                button_push = -1
                loop = False
                display_now = main_menu
    
    # ABOUT MODE 1
    if (running == True) and (display_now == info_mode1):

        display.fill(black)
        draw_info_mode1()
        pygame.display.flip()

        timer_start = time.time()
        timer_stop = 10

        loop = True
        
        while loop:
            waiting_sound.play()
            timer = time.time() - timer_start

            if timer > timer_stop:
                loop = False
                display_now = mode1
                        
    # MODE 1
    if (running == True) and (display_now == mode1):

        p1_points = int(0)
        p2_points = int(0)
        p3_points = int(0)
        p4_points = int(0)

        question_number = int(1)
        i = int(0)

        lines = open("/home/pi/Desktop/QUESTIONS.txt").readlines()
        questions = random.sample(lines, 25)

        loop = True

        while (loop):

            while question_number <= quenum:
                display.fill(black)

                background = pygame.image.load("/home/pi/Desktop/question-layout.png").convert()
                display.blit(background, background_position)

                line = questions[i]
                detail = line.split(",")

                num = textdraw(("Pytanie " + str(question_number)), 65, black, 25)
                question = textdraw((detail[0]), 100, black, 45)
                a = textdraw((detail[1]), 200, blue, 35)
                b = textdraw((detail[2]), 300, green, 35)
                c = textdraw((detail[3]), 400, yellow, 35)
                d = textdraw((detail[4]), 500, red, 35)

                ready = customtextdraw("Odpowiada:", (50,600), white, 25)
                player1 = customtextdraw("Gracz 1", (200,600), gray, 25)
                player2 = customtextdraw("Gracz 2", (400,600), gray, 25)
                player3 = customtextdraw("Gracz 3", (600,600), gray, 25)
                player4 = customtextdraw("Gracz 4", (800,600), gray, 25)

                correct = detail[5]

                question_sound.play()

                pygame.display.flip()

                button_push = -1

                loop2 = True

                #PLAYER 1
                while (loop2):
                    player1 = customtextdraw("Gracz 1", (200,600), green, 25)
                    player2 = customtextdraw("Gracz 2", (400,600), gray, 25)
                    player3 = customtextdraw("Gracz 3", (600,600), gray, 25)
                    player4 = customtextdraw("Gracz 4", (800,600), gray, 25)
                    pygame.display.flip()

                    if button_push == p1_blue:
                        button_push = -1
                        loop2 = False
                        p1_ans = "a"
                        print("p1 ok")
                        answer_sound.play()
                    elif button_push == p1_green:
                        button_push = -1
                        loop2 = False
                        p1_ans = "b"
                        print("p1 ok")
                        answer_sound.play()
                    elif button_push == p1_yellow:
                        button_push = -1
                        loop2 = False
                        p1_ans = "c"
                        print("p1 ok")
                        answer_sound.play()
                    elif button_push == p1_red:
                        button_push = -1
                        loop2 = False
                        p1_ans = "d"
                        print("p1 ok")
                        answer_sound.play()

                loop3 = True

                #PLAYER 2
                while (loop3):
                    player1 = customtextdraw("Gracz 1", (200,600), gray, 25)
                    player2 = customtextdraw("Gracz 2", (400,600), green, 25)
                    player3 = customtextdraw("Gracz 3", (600,600), gray, 25)
                    player4 = customtextdraw("Gracz 4", (800,600), gray, 25)
                    pygame.display.flip()

                    if button_push == p2_blue:
                        button_push = -1
                        loop3 = False
                        p2_ans = "a"
                        print("p2 ok")
                        answer_sound.play()
                    elif button_push == p2_green:
                        button_push = -1
                        loop3 = False
                        p2_ans = "b"
                        print("p2 ok")
                        answer_sound.play()
                    elif button_push == p2_yellow:
                        button_push = -1
                        loop3 = False
                        p2_ans = "c"
                        print("p2 ok")
                        answer_sound.play()
                    elif button_push == p2_red:
                        button_push = -1
                        loop3 = False
                        p2_ans = "d"
                        print("p2 ok")
                        answer_sound.play()

                loop4 = True

                #PLAYER 3
                while (loop4):
                    player1 = customtextdraw("Gracz 1", (200,600), gray, 25)
                    player2 = customtextdraw("Gracz 2", (400,600), gray, 25)
                    player3 = customtextdraw("Gracz 3", (600,600), green, 25)
                    player4 = customtextdraw("Gracz 4", (800,600), gray, 25)
                    pygame.display.flip()

                    if button_push == p3_blue:
                        button_push = -1
                        loop4 = False
                        p3_ans = "a"
                        print("p3 ok")
                        answer_sound.play()
                    elif button_push == p3_green:
                        button_push = -1
                        loop4 = False
                        p3_ans = "b"
                        print("p3 ok")
                        answer_sound.play()
                    elif button_push == p3_yellow:
                        button_push = -1
                        loop4 = False
                        p3_ans = "c"
                        print("p3 ok")
                        answer_sound.play()
                    elif button_push == p3_red:
                        button_push = -1
                        loop4 = False
                        p3_ans = "d"
                        print("p3 ok")
                        answer_sound.play()

                loop5 = True

                #PLAYER 4
                while (loop5):
                    player1 = customtextdraw("Gracz 1", (200,600), gray, 25)
                    player2 = customtextdraw("Gracz 2", (400,600), gray, 25)
                    player3 = customtextdraw("Gracz 3", (600,600), gray, 25)
                    player4 = customtextdraw("Gracz 4", (800,600), green, 25)
                    pygame.display.flip()

                    if button_push == p4_blue:
                        button_push = -1
                        loop5 = False
                        p4_ans = "a"
                        print("p4 ok")
                    elif button_push == p4_green:
                        button_push = -1
                        loop5 = False
                        p4_ans = "b"
                        print("p4 ok")
                    elif button_push == p4_yellow:
                        button_push = -1
                        loop5 = False
                        p4_ans = "c"
                        print("p4 ok")
                    elif button_push == p4_red:
                        button_push = -1
                        loop5 = False
                        p4_ans = "d"
                        print("p4 ok")

                if p1_ans == correct:
                    p1_points = p1_points + 10
                else:
                    p1_points = p1_points

                if p2_ans == correct:
                    p2_points = p2_points + 10
                else:
                    p2_points = p2_points

                if p3_ans == correct:
                    p3_points = p3_points + 10
                else:
                    p3_points = p3_points

                if p4_ans == correct:
                    p4_points = p4_points + 10
                else:
                    p4_points = p4_points

                question_number = question_number + 1
                i = i + 1
            
            print(p1_points)
            print(p2_points)
            print(p3_points)
            print(p4_points)

            loop = False
            display_now = results

    #QUESTIONS NUMBER MODE 2
    if (running == True) and (display_now == quenum_2):

        display.fill(black)
        draw_quenum()
        pygame.display.flip()

        loop = True
        
        while(loop):
            if (button_push == p1_blue):
                button_push = -1
                loop = False
                quenum = int(10)
                display_now = info_mode2

            if (button_push == p1_green):
                button_push = -1
                loop = False
                quenum = int(25)
                display_now = info_mode2

            if (button_push == p1_yellow):
                button_push = -1
                loop = False
                quenum = int(50)
                display_now = info_mode2

            if (button_push == p1_red):
                button_push = -1
                loop = False
                display_now = main_menu

    # ABOUT MODE 2
    if (running == True) and (display_now == info_mode2):

        display.fill(black)
        draw_info_mode2()
                
        pygame.display.flip()

        timer_start = time.time()
        timer_stop = 10

        loop = True
        
        while loop:
            waiting_sound.play()
            timer = time.time() - timer_start

            if timer > timer_stop:
                loop = False
                display_now = mode2

    # MODE 2
    if (running == True) and (display_now == mode2):

        p1_points = int(0)
        p2_points = int(0)
        p3_points = int(0)
        p4_points = int(0)

        quenum = int(5)
        question_number = int(1)
        i = int(0)

        lines = open("/home/pi/Desktop/QUESTIONS.txt").readlines()
        questions = random.sample(lines, 25)

        loop = True

        while (loop):

            while question_number <= quenum:
                display.fill(black)

                background = pygame.image.load("/home/pi/Desktop/question-layout.png").convert()
                display.blit(background, background_position)

                line = questions[i]
                detail = line.split(",")

                num = textdraw(("Pytanie " + str(question_number)), 65, black, 25)
                question = textdraw((detail[0]), 100, black, 45)
                a = textdraw((detail[1]), 200, blue, 35)
                b = textdraw((detail[2]), 300, green, 35)
                c = textdraw((detail[3]), 400, yellow, 35)
                d = textdraw((detail[4]), 500, red, 35)

                ready = customtextdraw("Odpowiada:", (50,600), white, 25)
                player1 = customtextdraw("Gracz 1", (200,600), gray, 25)
                player2 = customtextdraw("Gracz 2", (400,600), gray, 25)
                player3 = customtextdraw("Gracz 3", (600,600), gray, 25)
                player4 = customtextdraw("Gracz 4", (800,600), gray, 25)

                correct = detail[5]

                question_sound.play()

                pygame.display.flip()

                button_push = -1

                # CHOOSE PLAYER
                loop2 = True

                while (loop2):

                    if (button_push == p1_blue):
                        button_push = -1
                        loop2 = False
                        answering = "player1"
                        declaration_sound.play()
                    elif (button_push == p2_blue):
                        button_push = -1
                        loop2 = False
                        answering = "player2"
                        declaration_sound.play()
                    elif (button_push == p3_blue):
                        button_push = -1
                        loop2 = False
                        answering = "player3"
                        declaration_sound.play()
                    elif (button_push == p4_blue):
                        button_push = -1
                        loop2 = False
                        answering = "player4"
                        declaration_sound.play()

                button_push = -1

                loop3 = True

                while (loop3):
                    if (answering == "player1"):
                        player1 = customtextdraw("Gracz 1", (200,600), green, 25)
                        player2 = customtextdraw("Gracz 2", (400,600), gray, 25)
                        player3 = customtextdraw("Gracz 3", (600,600), gray, 25)
                        player4 = customtextdraw("Gracz 4", (800,600), gray, 25)
                        pygame.display.flip()

                        if button_push == p1_blue:
                            button_push = -1
                            loop3 = False
                            p1_ans = "a"
                            if (p1_ans == correct):
                                p1_points = p1_points + 10
                            else:
                                break
                            print("p1 ok")
                        elif button_push == p1_green:
                            button_push = -1
                            loop3 = False
                            p1_ans = "b"
                            if (p1_ans == correct):
                                p1_points = p1_points + 10
                            else:
                                break
                            print("p1 ok")
                        elif button_push == p1_yellow:
                            button_push = -1
                            loop3 = False
                            p1_ans = "c"
                            if (p1_ans == correct):
                                p1_points = p1_points + 10
                            else:
                                break
                            print("p1 ok")
                        elif button_push == p1_red:
                            button_push = -1
                            loop3 = False
                            p1_ans = "d"
                            if (p1_ans == correct):
                                p1_points = p1_points + 10
                            else:
                                break
                            print("p1 ok")
                        
                    elif (answering == "player2"):
                        player1 = customtextdraw("Gracz 1", (200,600), gray, 25)
                        player2 = customtextdraw("Gracz 2", (400,600), green, 25)
                        player3 = customtextdraw("Gracz 3", (600,600), gray, 25)
                        player4 = customtextdraw("Gracz 4", (800,600), gray, 25)
                        pygame.display.flip()

                        if button_push == p2_blue:
                            button_push = -1
                            loop3 = False
                            p2_ans = "a"
                            if (p2_ans == correct):
                                p2_points = p2_points + 10
                            else:
                                break
                            print("p2 ok")
                        elif button_push == p2_green:
                            button_push = -1
                            loop3 = False
                            p2_ans = "b"
                            if (p2_ans == correct):
                                p2_points = p2_points + 10
                            else:
                                break
                            print("p2 ok")
                        elif button_push == p2_yellow:
                            button_push = -1
                            loop3 = False
                            p2_ans = "c"
                            if (p2_ans == correct):
                                p2_points = p2_points + 10
                            else:
                                break
                            print("p2 ok")
                        elif button_push == p2_red:
                            button_push = -1
                            loop3 = False
                            p2_ans = "d"
                            if (p2_ans == correct):
                                p2_points = p2_points + 10
                            else:
                                break
                            print("p2 ok")

                    elif (answering == "player3"):
                        player1 = customtextdraw("Gracz 1", (200,600), gray, 25)
                        player2 = customtextdraw("Gracz 2", (400,600), gray, 25)
                        player3 = customtextdraw("Gracz 3", (600,600), green, 25)
                        player4 = customtextdraw("Gracz 4", (800,600), gray, 25)
                        pygame.display.flip()

                        if button_push == p3_blue:
                            button_push = -1
                            loop3 = False
                            p3_ans = "a"
                            if (p3_ans == correct):
                                p3_points = p3_points + 10
                            else:
                                break
                            print("p3 ok")
                        elif button_push == p3_green:
                            button_push = -1
                            loop3 = False
                            p3_ans = "b"
                            if (p3_ans == correct):
                                p3_points = p3_points + 10
                            else:
                                break
                            print("p3 ok")
                        elif button_push == p3_yellow:
                            button_push = -1
                            loop3 = False
                            p3_ans = "c"
                            if (p3_ans == correct):
                                p3_points = p3_points + 10
                            else:
                                break
                            print("p3 ok")
                        elif button_push == p3_red:
                            button_push = -1
                            loop3 = False
                            p3_ans = "d"
                            if (p3_ans == correct):
                                p3_points = p3_points + 10
                            else:
                                break
                            print("p3 ok")

                    elif (answering == "player4"):
                        player1 = customtextdraw("Gracz 1", (200,600), gray, 25)
                        player2 = customtextdraw("Gracz 2", (400,600), gray, 25)
                        player3 = customtextdraw("Gracz 3", (600,600), gray, 25)
                        player4 = customtextdraw("Gracz 4", (800,600), green, 25)
                        pygame.display.flip()

                        if button_push == p4_blue:
                            button_push = -1
                            loop3 = False
                            p4_ans = "a"
                            if (p4_ans == correct):
                                p4_points = p4_points + 10
                            else:
                                break
                            print("p4 ok")
                        elif button_push == p4_green:
                            button_push = -1
                            loop3 = False
                            p4_ans = "b"
                            if (p4_ans == correct):
                                p4_points = p4_points + 10
                            else:
                                break
                            print("p4 ok")
                        elif button_push == p4_yellow:
                            button_push = -1
                            loop3 = False
                            p4_ans = "c"
                            if (p4_ans == correct):
                                p4_points = p4_points + 10
                            else:
                                break
                            print("p4 ok")
                        elif button_push == p4_red:
                            button_push = -1
                            loop3 = False
                            p4_ans = "d"
                            if (p4_ans == correct):
                                p4_points = p4_points + 10
                            else:
                                break
                            print("p4 ok")

                question_number = question_number + 1
                i = i + 1

            print(p1_points)
            print(p2_points)
            print(p3_points)
            print(p4_points)

            loop = False
            display_now = results

    # RESULTS
    if (running == True) and (display_now == results):
        display.fill(black)
        results_sound.play()

        background = pygame.image.load("/home/pi/Desktop/layout-results.png").convert()
        display.blit(background, background_position)

        scores = [('Gracz 1', p1_points),
            ('Gracz 2', p2_points),
            ('Gracz 3', p3_points),
            ('Gracz 4', p4_points)]

        def sort_key(score):
            return score[1]

        scores.sort(key=sort_key, reverse=True)

        def scoring(x):
            scr = str(scores[x][0]) + "    " + str(scores[x][1]) + " pkt"
            return scr
        
        results = textdraw("Wyniki", 100, white, 45)

        first = textdraw(scoring(0), 250, magenta, 45)
        second = textdraw(scoring(1), 350, magenta, 45)
        third = textdraw(scoring(2), 450, magenta, 45)
        fourth = textdraw(scoring(3), 550, magenta, 45)

        quit = textdraw("powrót do menu", 650, red, 25)

        pygame.display.flip()

        loop = True

        while(loop):
            if (button_push == p1_red):
                button_push = -1
                loop = False
                display_now = main_menu

pygame.quit()
