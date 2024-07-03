import pygame
import os
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
display_info = pygame.display.Info()

WIDTH, HEIGHT = display_info.current_w, display_info.current_h

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT - 50), pygame.RESIZABLE)
pygame.display.set_caption("LUDO Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

click_x = 0
click_y = 0

yellow_turn = True
green__turn = False
red_turn = False
blue_turn = False

y1x, y1y = 100, 100
y2x, y2y = 204, 100
y3x, y3y = 100, 204
y4x, y4y = 204, 204

g1x, g1y = 532, 100
g2x, g2y = 636, 100
g3x, g3y = 532, 204
g4x, g4y = 636, 204

r1x, r1y = 532, 532
r2x, r2y = 636, 532
r3x, r3y = 532, 636
r4x, r4y = 636, 636

b1x, b1y = 100, 532
b2x, b2y = 100, 636
b3x, b3y = 204, 532
b4x, b4y = 204, 636

y1 = None
y2 = None
y3 = None
y4 = None

g1 = None
g2 = None
g3 = None
g4 = None

r1 = None
r2 = None
r3 = None
r4 = None

b1 = None
b2 = None
b3 = None
b4 = None

y1_trun = False
y2_trun = False
y3_trun = False
y4_trun = False

g1_trun = False
g2_trun = False
g3_trun = False
g4_trun = False

r1_trun = False
r2_trun = False
r3_trun = False
r4_trun = False

b1_trun = False
b2_trun = False
b3_trun = False
b4_trun = False

#Loading the FOnt
bigsize = 55
smallsize = 25  

FONT = pygame.font.SysFont('comicsans', bigsize)
FONT_s = pygame.font.SysFont('comicsans', 25)

#Loasding all the images
DICE_SIZE = 100
Dice1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Dice1.png')), (DICE_SIZE, DICE_SIZE))
Dice2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Dice 2.png')), (DICE_SIZE, DICE_SIZE))
Dice3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Dice3.png')), (DICE_SIZE, DICE_SIZE))
Dice4 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Dice4.png')), (DICE_SIZE, DICE_SIZE))
Dice5 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Dice 5.png')), (DICE_SIZE, DICE_SIZE))
Dice6 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Dice 6.png')), (DICE_SIZE, DICE_SIZE))

dice_rect = None

def draw_dice(random_number1):
    dice_offset = 100
    dice_offset2 = 110 + DICE_SIZE
    DICE_POS_X = WINDOW.get_width() * 0.75 - DICE_SIZE/2 + dice_offset - dice_offset/3
    DICE_POS_Y = WINDOW.get_height() * 0.1 - DICE_SIZE/2

    global dice_rect
    dice_rect = pygame.draw.rect(WINDOW, WHITE, [DICE_POS_X + dice_offset, DICE_POS_Y + DICE_SIZE + 10, DICE_SIZE*2 + (dice_offset2 - DICE_SIZE*2), DICE_SIZE/2], 3)
    roll_dice_text = FONT_s.render("Roll Dice", True, WHITE)
    WINDOW.blit(roll_dice_text, [(DICE_POS_X + dice_offset) + (DICE_SIZE*2 + (dice_offset2 - DICE_SIZE*2)) / 2 - roll_dice_text.get_width()/2, DICE_POS_Y + DICE_SIZE + 15])
        
    if random_number1 == 1:
        WINDOW.blit(Dice1, [DICE_POS_X + dice_offset, DICE_POS_Y])
    elif random_number1 == 2:
        WINDOW.blit(Dice2, [DICE_POS_X + dice_offset, DICE_POS_Y])
    elif random_number1 == 3:
        WINDOW.blit(Dice3, [DICE_POS_X + dice_offset, DICE_POS_Y])
    elif random_number1 == 4:
        WINDOW.blit(Dice4, [DICE_POS_X + dice_offset, DICE_POS_Y])
    elif random_number1 == 5:
        WINDOW.blit(Dice5, [DICE_POS_X + dice_offset, DICE_POS_Y])
    elif random_number1 == 6:
        WINDOW.blit(Dice6, [DICE_POS_X + dice_offset, DICE_POS_Y])

def board_draw():
    global click_y, click_x
    global y1x, y1y, y2x, y2y, y3x, y3y, y4x, y4y

    # WINDOW.fill((255, 255, 255)) to make the color of the screen white
    

    # drawing the board
    pygame.draw.rect(WINDOW, (255, 255, 255), (0, 0, 736, 736), width=8)  # Main Rectangle

    # Green Small Boxes
    pygame.draw.rect(WINDOW, (0, 255, 0), (392, 56, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (0, 255, 0), (344, 56, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (0, 255, 0), (344, 104, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (0, 255, 0), (344, 152, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (0, 255, 0), (344, 200, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (0, 255, 0), (344, 248, 48, 48), width=48)

    # Red Small Boxes
    pygame.draw.rect(WINDOW, (255, 0, 0), (440, 344, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (255, 0, 0), (488, 344, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (255, 0, 0), (536, 344, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (255, 0, 0), (584, 344, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (255, 0, 0), (632, 344, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (255, 0, 0), (632, 392, 48, 48), width=48)

    # Blue Small Boxes
    pygame.draw.rect(WINDOW, (0, 0, 255), (344, 440, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (0, 0, 255), (344, 488, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (0, 0, 255), (344, 536, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (0, 0, 255), (344, 584, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (0, 0, 255), (344, 632, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (0, 0, 255), (296, 632, 48, 48), width=48)

    # Yellow Small Boxes
    pygame.draw.rect(WINDOW, (255, 255, 0), (56, 296, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (255, 255, 0), (56, 344, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (255, 255, 0), (104, 344, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (255, 255, 0), (152, 344, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (255, 255, 0), (200, 344, 48, 48), width=48)
    pygame.draw.rect(WINDOW, (255, 255, 0), (248, 344, 48, 48), width=48)

    # Yellow Player
    pygame.draw.rect(WINDOW, (255, 255, 0), (8, 8, 288, 288), width=48)
    pygame.draw.rect(WINDOW, (255, 255, 255), (56, 56, 192, 192), width=2)

    # Yellow Pegs Outer Circle
    pygame.draw.circle(WINDOW, (255, 255, 255), (y1x, y1y), 24, width=5)  # First
    pygame.draw.circle(WINDOW, (255, 255, 255), (y2x, y2y), 24, width=5)  # Second
    pygame.draw.circle(WINDOW, (255, 255, 255), (y3x, y3y), 24, width=5)  # Third
    pygame.draw.circle(WINDOW, (255, 255, 255), (y4x, y4y), 24, width=5)  # Fourth

    # Yellow Pegs Inner Circle
    global y1, y2, y3, y4
    y1 = pygame.draw.circle(WINDOW, (255, 255, 0), (y1x, y1y), 16)  # First
    y2 = pygame.draw.circle(WINDOW, (255, 255, 0), (y2x, y2y), 16)  # Second
    y3 = pygame.draw.circle(WINDOW, (255, 255, 0), (y3x, y3y), 16)  # Third
    y4 = pygame.draw.circle(WINDOW, (255, 255, 0), (y4x, y4y), 16)  # Fourth

    # Green Player
    pygame.draw.rect(WINDOW, (0, 255, 0), (440, 8, 288, 288), width=48)
    pygame.draw.rect(WINDOW, (255, 255, 255), (488, 56, 192, 192), width=2)

    # Green Pegs Outer Circle
    pygame.draw.circle(WINDOW, (255, 255, 255), (g1x, g1y), 24, width=1)  # First
    pygame.draw.circle(WINDOW, (255, 255, 255), (g2x, g2y), 24, width=1)  # Second
    pygame.draw.circle(WINDOW, (255, 255, 255), (g3x, g3y), 24, width=1)  # Third
    pygame.draw.circle(WINDOW, (255, 255, 255), (g4x, g4y), 24, width=1)  # Fourth

    global g1, g2, g3, g4
    # Green Pegs Inner Circle
    g1 = pygame.draw.circle(WINDOW, (0, 255, 0), (g1x, g1y), 16)  # First
    g2 = pygame.draw.circle(WINDOW, (0, 255, 0), (g2x, g2y), 16)  # Secondw
    g3 = pygame.draw.circle(WINDOW, (0, 255, 0), (g3x, g3y), 16)  # Third
    g4 = pygame.draw.circle(WINDOW, (0, 255, 0), (g4x, g4y), 16)  # Fourth

    # Blue Player
    pygame.draw.rect(WINDOW, (0, 0, 255), (8, 440, 288, 288), width=48)
    pygame.draw.rect(WINDOW, (255, 255, 255), (56, 488, 192, 192), width=2)  # border_radius for rounded effect

    # Blue Pegs Outer Circle
    pygame.draw.circle(WINDOW, (255, 255, 255), (b1x, b1y), 24, width=1)  # First
    pygame.draw.circle(WINDOW, (255, 255, 255), (b2x, b2y), 24, width=1)  # Second
    pygame.draw.circle(WINDOW, (255, 255, 255), (b3x, b3y), 24, width=1)  # Third
    pygame.draw.circle(WINDOW, (255, 255, 255), (b4x, b4y), 24, width=1)  # Fourth

    global b1, b2, b3, b4
    # Blue Pegs Inner Circle
    b1 = pygame.draw.circle(WINDOW, (0, 0, 255), (b1x, b1y), 16)  # First
    b2 = pygame.draw.circle(WINDOW, (0, 0, 255), (b2x, b2y), 16)  # Second
    b3 = pygame.draw.circle(WINDOW, (0, 0, 255), (b3x, b3y), 16)  # Third
    b4 = pygame.draw.circle(WINDOW, (0, 0, 255), (b4x, b4y), 16)  # Fourth

    # Red Player
    pygame.draw.rect(WINDOW, (255, 0, 0), (440, 440, 288, 288), width=48)
    pygame.draw.rect(WINDOW, (255, 255, 255), (488, 488, 192, 192), width=2)

    # Red Pegs Outer Circle
    pygame.draw.circle(WINDOW, (255, 255, 255), (r1x, r1y), 24, width=1)  # First
    pygame.draw.circle(WINDOW, (255, 255, 255), (r2x, r2y), 24, width=1)  # Second
    pygame.draw.circle(WINDOW, (255, 255, 255), (r3x, r3y), 24, width=1)  # Third
    pygame.draw.circle(WINDOW, (255, 255, 255), (r4x, r4y), 24, width=1)  # Fourth

    global r1, r2, r3, r4
    # Red Pegs Inner Circle
    r1 = pygame.draw.circle(WINDOW, (255, 0, 0), (r1x, r1y), 16)  # First
    r2 = pygame.draw.circle(WINDOW, (255, 0, 0), (r2x, r2y), 16)  # Second
    r3 = pygame.draw.circle(WINDOW, (255, 0, 0), (r3x, r3y), 16)  # Third
    r4 = pygame.draw.circle(WINDOW, (255, 0, 0), (r4x, r4y), 16)  # Fourth

    # Home Box
    pygame.draw.rect(WINDOW, (255, 255, 255), (296, 296, 144, 144), width=1)

    # Lines For The Middle Cross
    pygame.draw.line(WINDOW, (255, 255, 255), (296, 296), (440, 440))
    pygame.draw.line(WINDOW, (255, 255, 255), (440, 296), (296, 440))

    

    # Small Boxes Lines Between Yellow And Green
    pygame.draw.line(WINDOW, (255, 255, 255), (296, 56), (440, 56))
    pygame.draw.line(WINDOW, (255, 255, 255), (296, 104), (440, 104))
    pygame.draw.line(WINDOW, (255, 255, 255), (296, 152), (440, 152))
    pygame.draw.line(WINDOW, (255, 255, 255), (296, 200), (440, 200))
    pygame.draw.line(WINDOW, (255, 255, 255), (296, 248), (440, 248))

    # Small Boxes Lines Between Blue And Red
    pygame.draw.line(WINDOW, (255, 255, 255), (296, 488), (440, 488))
    pygame.draw.line(WINDOW, (255, 255, 255), (296, 536), (440, 536))
    pygame.draw.line(WINDOW, (255, 255, 255), (296, 584), (440, 584))
    pygame.draw.line(WINDOW, (255, 255, 255), (296, 632), (440, 632))
    pygame.draw.line(WINDOW, (255, 255, 255), (296, 680), (440, 680))

    # Small Boxes Lines Between Yellow And Blue
    pygame.draw.line(WINDOW, (255, 255, 255), (56, 296), (56, 440))
    pygame.draw.line(WINDOW, (255, 255, 255), (104, 296), (104, 440))
    pygame.draw.line(WINDOW, (255, 255, 255), (152, 296), (152, 440))
    pygame.draw.line(WINDOW, (255, 255, 255), (200, 296), (200, 440))
    pygame.draw.line(WINDOW, (255, 255, 255), (248, 296), (248, 440))


    # Box Vertical Lines
    #                              color       s_x, s_y   e_x, e_y   
    pygame.draw.line(WINDOW, (255, 255, 255), (344, 8), (344, 296))
    pygame.draw.line(WINDOW, (255, 255, 255), (392, 8), (392, 296))

    pygame.draw.line(WINDOW, (255, 255, 255), (344, 440), (344, 728))
    pygame.draw.line(WINDOW, (255, 255, 255), (392, 440), (392, 728))

    pygame.draw.line(WINDOW, (255, 255, 255), (8, 344), (296, 344))
    pygame.draw.line(WINDOW, (255, 255, 255), (8, 392), (296, 392))

    pygame.draw.line(WINDOW, (255, 255, 255), (440, 344), (728, 344))
    pygame.draw.line(WINDOW, (255, 255, 255), (440, 392), (728, 392))

    # Small Boxes Lines Between Green And Red
    pygame.draw.line(WINDOW, (255, 255, 255), (488, 296), (488, 440))
    pygame.draw.line(WINDOW, (255, 255, 255), (536, 296), (536, 440))
    pygame.draw.line(WINDOW, (255, 255, 255), (584, 296), (584, 440))
    pygame.draw.line(WINDOW, (255, 255, 255), (632, 296), (632, 440))
    pygame.draw.line(WINDOW, (255, 255, 255), (680, 296), (680, 440))

    if red_turn:
        pygame.draw.rect(WINDOW, RED, [0, 0, WINDOW.get_width(), WINDOW.get_height()], 5)
    elif green__turn:
        pygame.draw.rect(WINDOW, GREEN, [0, 0, WINDOW.get_width(), WINDOW.get_height()], 5)
    elif blue_turn:
        pygame.draw.rect(WINDOW, BLUE, [0, 0, WINDOW.get_width(), WINDOW.get_height()], 5)
    elif yellow_turn:
        pygame.draw.rect(WINDOW, YELLOW, [0, 0, WINDOW.get_width(), WINDOW.get_height()], 5)


def player_movement(pos_x, pos_y, random_number):
    temp_x = pos_x
    temp_y = pos_y
    
    global yellow_turn, green__turn, red_turn, blue_turn, y1_trun, y2_trun, y3_trun, y4_trun
    global y1x, y1y, y2x, y2y, y3x, y3y, y4x, y4y, g4y, g1x, g1y, g2x, g2y, g3x, g3y, g4x, g4y
    global r1x, r1y, r2x, r2y, r3x, r3y, r4x, r4y, b4y, b1x, b1y, b2x, b2y, b3x, b3y, b4x, b4y


    while random_number > 0:
        print(random_number)

        if temp_y < 344 and temp_x < 296 and temp_y > 296:
            temp_x += 48  
            if temp_x > 295:
                temp_y -= 48
            print("move: 1")

        #Green's house
        elif temp_x > 344 and temp_x < 392 and temp_y < 296 and green__turn:
            temp_y += 48

        elif temp_x > 296 and temp_x < 344 and temp_y > 56  and temp_y < 296:
            temp_y -= 48
            print("move: 2")
        
        elif temp_x < 392 and temp_y < 56:
            temp_x += 48
            print("move: 3")

        elif temp_x > 392 and temp_y < 296 and temp_x < 440:
            temp_y += 48
            if temp_y > 296:
                temp_x += 48
            print("move: 4")

        elif temp_x < 680 and temp_y < 344 and temp_y > 296 :
            temp_x += 48
            print("move: 5")
        
        #red's house
        elif temp_y > 344 and temp_y < 392 and temp_x > 440 and red_turn:
            temp_x -= 48

        elif temp_y < 392 and temp_x > 680 and temp_y > 296 :
            temp_y += 48
            print("move: 6")
        
        elif temp_y > 392 and temp_x > 440 and temp_y < 440:
            temp_x -= 48
            if temp_x < 440:
                temp_y += 48
            print("move: 7")

        elif temp_y < 680 and temp_x > 392 and temp_x < 440 and temp_y > 440:
            temp_y += 48   
            print("move: 8")

        #Blue's house
        elif temp_x < 392 and temp_x > 344 and temp_y > 440 and blue_turn:
            temp_y -= 48 
        
        elif temp_y > 680 and temp_x > 344:
            temp_x -= 48
            print("move: 9")
        
        elif temp_y > 440 and temp_x < 344 and temp_y < 728 and temp_x > 296:
            temp_y -= 48
            if temp_y < 440:
                temp_x -= 48
            print("move: 10")

        elif temp_y > 392 and temp_y < 440 and temp_x > 56 and temp_x < 344:
            temp_x -= 48
            print("move: 11")


        #yellow's house
        elif temp_x < 344 and temp_y > 344 and temp_y < 392 and yellow_turn:
            temp_x += 48

        elif temp_x < 56 and temp_y > 344 and temp_y < 440:
            temp_y -= 48
            print("move: 12")


        if temp_x < 296 and temp_y < 296 and random_number == 6:
            temp_x = 80
            temp_y = 320

            random_number = 0
        elif temp_x > 440 and temp_y < 296 and random_number == 6:
            temp_x = 416
            temp_y = 80

            random_number = 0
        elif temp_x > 440 and temp_y > 440 and random_number == 6:
            temp_x = 656
            temp_y = 416

            random_number = 0
        elif temp_x < 296 and temp_y > 440 and random_number == 6:
            temp_x = 320
            temp_y = 656

            random_number = 0

        if yellow_turn:
            if y1_trun:
                y1x = temp_x
                y1y = temp_y
            elif y2_trun:
                y2x = temp_x
                y2y = temp_y
            elif y3_trun:
                y3x = temp_x
                y3y = temp_y
            elif y4_trun:
                y4x = temp_x
                y4y = temp_y
        elif green__turn:
            if g1_trun:
                g1x = temp_x
                g1y = temp_y
            elif g2_trun:
                g2x = temp_x
                g2y = temp_y
            elif g3_trun:
                g3x = temp_x
                g3y = temp_y
            elif g4_trun:
                g4x = temp_x
                g4y = temp_y
        elif red_turn:
            if r1_trun:
                r1x = temp_x
                r1y = temp_y
            elif r2_trun:
                r2x = temp_x
                r2y = temp_y
            elif r3_trun:
                r3x = temp_x
                r3y = temp_y
            elif r4_trun:
                r4x = temp_x
                r4y = temp_y
        elif blue_turn:
            if b1_trun:
                b1x = temp_x
                b1y = temp_y
            elif b2_trun:
                b2x = temp_x
                b2y = temp_y
            elif b3_trun:
                b3x = temp_x
                b3y = temp_y
            elif b4_trun:
                b4x = temp_x
                b4y = temp_y


        print(temp_x, ", ", temp_y)
        WINDOW.fill((0, 0, 0))

        board_draw()
        draw_dice(random_number)

        pygame.display.update()

        pygame.time.delay(200)

        random_number -= 1


def main():
    random_number = 0
    global click_x, click_y, yellow_turn, green__turn, red_turn, blue_turn, y1_trun, y2_trun, y3_trun, y4_trun, g1_trun, g2_trun, g3_trun, g4_trun
    global r1_trun, r2_trun, r3_trun, r4_trun, b1_trun, b2_trun, b3_trun, b4_trun

    sure_clicked = False
    cheating = False
    click1 = False
    clicked = False

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and cheating == False:
                    cheating = True
                elif event.key == pygame.K_c and cheating == True:
                    cheating = False

                if event.key == pygame.K_SPACE and cheating == False and clicked == False:
                    random_number = random.randint(1, 6)
                    print(random_number)

                    clicked = True

                if cheating:
                    if event.key == pygame.K_1 and click1 == False:
                        random_number = 1
                        click1 = True
                    elif event.key == pygame.K_2 and click1 == False:
                        random_number = 2
                        click1 = True
                    elif event.key == pygame.K_3 and click1 == False:
                        random_number = 3
                        click1 = True
                    elif event.key == pygame.K_4 and click1 == False:
                        random_number = 4
                        click1 = True
                    elif event.key == pygame.K_5 and click1 == False:
                        random_number = 5
                        click1 = True
                    elif event.key == pygame.K_6 and click1 == False:
                        random_number = 6
                        click1 = True
                    
                    if click1:
                        clicked = True
                        click1 = False
                    else:
                        clicked = False
                    
                    print(random_number)

            if event.type == pygame.MOUSEBUTTONDOWN:
            #    print(event)
               click_x = event.pos[0]
               click_y = event.pos[1]
 
               print(click_x, " ", click_y)

        draw_dice(random_number)
        board_draw()

        global y1, y2, y3, y4
        global g1, g2, g3, g4
        global r1, r2, r3, r4
        global b1, b2, b3, b4
        
        if yellow_turn and clicked == True:
            if y1.collidepoint(click_x, click_y):
                y1_trun = True
                player_movement(y1x, y1y, random_number)
                y1_trun = False
                sure_clicked = True

            elif y2.collidepoint(click_x, click_y):
                y2_trun = True
                player_movement(y2x, y2y, random_number)
                y2_trun = False
                sure_clicked = True

            elif y3.collidepoint(click_x, click_y):
                y3_trun = True
                player_movement(y3x, y3y, random_number)
                y3_trun = False
                sure_clicked = True

            elif y4.collidepoint(click_x, click_y):
                y4_trun = True
                player_movement(y4x, y4y, random_number)
                y4_trun = False
                sure_clicked = True

            if sure_clicked:
                clicked = False
                sure_clicked = False

                if random_number != 6:
                    yellow_turn = False
                    green__turn = True

                print("Clicked False")

        
        elif green__turn and clicked == True:
            if g1.collidepoint(click_x, click_y):
                g1_trun = True
                player_movement(g1x, g1y, random_number)
                g1_trun = False
                sure_clicked = True

            elif g2.collidepoint(click_x, click_y):
                g2_trun = True
                player_movement(g2x, g2y, random_number)
                g2_trun = False
                sure_clicked = True

            elif g3.collidepoint(click_x, click_y):
                g3_trun = True
                player_movement(g3x, g3y, random_number)
                g3_trun = False
                sure_clicked = True

            elif g4.collidepoint(click_x, click_y):
                g4_trun = True
                player_movement(g4x, g4y, random_number)
                g4_trun = False
                sure_clicked = True

            if sure_clicked:
                clicked = False
                sure_clicked = False
                print("Clicked False")

                if random_number != 6:
                    green__turn = False
                    red_turn = True


        elif red_turn and clicked == True:
            if r1.collidepoint(click_x, click_y):
                r1_trun = True
                player_movement(r1x, r1y, random_number)
                r1_trun = False
                sure_clicked = True

            elif r2.collidepoint(click_x, click_y):
                r2_trun = True
                player_movement(r2x, r2y, random_number)
                r2_trun = False
                sure_clicked = True

            elif r3.collidepoint(click_x, click_y):
                r3_trun = True
                player_movement(r3x, r3y, random_number)
                r3_trun = False
                sure_clicked = True

            elif r4.collidepoint(click_x, click_y):
                r4_trun = True
                player_movement(r4x, r4y, random_number)
                r4_trun = False
                sure_clicked = True

            if sure_clicked:
                clicked = False
                sure_clicked = False
                print("Clicked False")

                if random_number != 6:
                    red_turn = False
                    blue_turn = True


        elif blue_turn and clicked == True:
            if b1.collidepoint(click_x, click_y):
                b1_trun = True
                player_movement(b1x, b1y, random_number)
                b1_trun = False
                sure_clicked = True

            elif b2.collidepoint(click_x, click_y):
                b2_trun = True
                player_movement(b2x, b2y, random_number)
                b2_trun = False
                sure_clicked = True

            elif b3.collidepoint(click_x, click_y):
                b3_trun = True
                player_movement(b3x, b3y, random_number)
                b3_trun = False
                sure_clicked = True

            elif b4.collidepoint(click_x, click_y):
                b4_trun = True
                player_movement(b4x, b4y, random_number)
                b4_trun = False
                sure_clicked = True

            if sure_clicked:
                clicked = False
                sure_clicked = False
                print("Clicked False")

                if random_number != 6:
                    blue_turn = False
                    yellow_turn = True

        pygame.display.update()


main()