import pygame

pygame.mixer.init()

# SOUNDS
question_sound = pygame.mixer.Sound("/home/pi/Desktop/RPI Quiz Game/que.mp3")
answer_sound = pygame.mixer.Sound("/home/pi/Desktop/RPI Quiz Game/ans.mp3")
results_sound = pygame.mixer.Sound("/home/pi/Desktop/RPI Quiz Game/app.mp3")
waiting_sound = pygame.mixer.Sound("/home/pi/Desktop/RPI Quiz Game/wait.mp3")
declaration_sound = pygame.mixer.Sound("/home/pi/Desktop/RPI Quiz Game/dec.mp3")

#IMAGES
layout_menu = "/home/pi/Desktop/RPI Quiz Game/layout-menu.png"
layout_waiting = "/home/pi/Desktop/RPI Quiz Game/layout-waiting.png"
layout_details = "/home/pi/Desktop/RPI Quiz Game/details-layout.png"
layout_start = "/home/pi/Desktop/RPI Quiz Game/start-layout.png"
layout_question = "/home/pi/Desktop/RPI Quiz Game/question-layout.png"
layout_modes = "/home/pi/Desktop/RPI Quiz Game/modes-layout.png"

# COLORS
black = (0, 0, 0)
gray = (127, 127, 127)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

# DISPLAY
background_position = [0,0]
width = 1100
height = 700

# SCREENS
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
modes = 14

# PLAYERS BUTTONS
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

# POINTS 
p1_points = int(0)
p2_points = int(0)
p3_points = int(0)
p4_points = int(0)

question_number = int(1)
