import sys
import pygame
import os
import random

import board 

pygame.init()
pygame.font.init()
pygame.mixer.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
display_info = pygame.display.Info()

WIDTH, HEIGHT = display_info.current_w, display_info.current_h
# WIDTH, HEIGHT = 900, 700

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT - 50), pygame.RESIZABLE)
pygame.display.set_caption("Business - The Board Game")

FPS = 60

BOARD_START_POS, BOARD_SIZE, CORNER_SQ_SIZE, MID_RECT_WIDTH, MID_RECT_HEIGHT =  board.give_varialbes(WINDOW)

clock = pygame.time.Clock()

#Loading the FOnt
bigsize = 55
smallsize = 25  

FONT = pygame.font.SysFont('comicsans', bigsize)
FONT_s = pygame.font.SysFont('comicsans', 25)


#Inlcuding the color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#definging player constatn positions
player_offset = 10


#movement variables
bottom_line_y = int(BOARD_SIZE - CORNER_SQ_SIZE + player_offset*3)
top_line_y = int(CORNER_SQ_SIZE - player_offset*3)
left_line_x = int(WINDOW.get_width() * BOARD_START_POS + CORNER_SQ_SIZE) - player_offset*3
right_line_x =  int(WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE + player_offset*3)

#end point of the image rectangle in the game card, made to adjust the rectangle according  to the device's size
rect_end =  MID_RECT_WIDTH*7
random_number1 = 0
random_number2 = 0
clicked = False

# red_x, red_y = WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE + player_offset*3  , BOARD_SIZE - CORNER_SQ_SIZE + player_offset*5
red_x, red_y = right_line_x , bottom_line_y
green_x, green_y = right_line_x , bottom_line_y
blue_x, blue_y = right_line_x , bottom_line_y
yellow_x, yellow_y = right_line_x , bottom_line_y

red_start = 0
green_start = 0
blue_start = 0
yellow_start = 0

total_random = 0

#properties varialbes
red_properties_owned = 0
green_properties_owned = 0
blue_properties_owned = 0
yellow_properties_owned = 0

#player turn
red_turn = True
green_turn = False
blue_turn = False
yellow_turn = False

red_net_worth = 0
green_net_worth = 0
blue_net_worth = 0
yellow_net_worth = 0

player_turn = ""

colors = ["red", "green", "blue", "yellow", "bank"]
player_list = []

cities_list = ["agra", "ahmedabad", "airways", "amritsar", "aurangabad", "bikaner", "chennai", "cochin", "darjeling", "electric", "goa", "guwahati", "hydrabad", "jaipur", "kolkatta", "lakshadweep", "mumbai", "mysore", "newdelhi", "pune", "railways", "roadways", "shimla", "udaipur", "varanasi", "waterways"]
city_list = []
city_name_var = "None"

starting_money = 40000

#Loasding all the images
DICE_SIZE = 100
Dice1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Dice1.png')), (DICE_SIZE, DICE_SIZE))
Dice2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Dice 2.png')), (DICE_SIZE, DICE_SIZE))
Dice3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Dice3.png')), (DICE_SIZE, DICE_SIZE))
Dice4 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Dice4.png')), (DICE_SIZE, DICE_SIZE))
Dice5 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Dice 5.png')), (DICE_SIZE, DICE_SIZE))
Dice6 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Dice 6.png')), (DICE_SIZE, DICE_SIZE))

# BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bg_img.png')), (WINDOW.get_width(), WINDOW.get_height()))


def re_size_image(image_name, img_size_height, img_size_width, pos_x, pos_y):
    image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', image_name)), (img_size_height, img_size_width))
    WINDOW.blit(image, [pos_x, pos_y])
    
def re_size_image_city(image_name, img_size_height, img_size_width, pos_x, pos_y, rotate = 0):
    image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Business_images',image_name)), (img_size_height, img_size_width))
    WINDOW.blit(image, [pos_x, pos_y])


def draw_rectangle(start_pos_x, start_pos_y, end_pos_x, end_pos_y):
    widht = end_pos_x - start_pos_x
    hight = end_pos_y - start_pos_y
    pygame.draw.rect(WINDOW, WHITE, [start_pos_x, start_pos_y, widht, hight], 3)

    
def open_file(filename, number):
    with open(os.path.join('Assets', 'Properties', filename), 'w') as city_file:
        city_file.write(str(number))


def open_city_file(mode, filename):

    global city_list

    if mode == 'r':
        with open(os.path.join('Assets' , 'City_files', filename), 'r') as file:
            data = file.read()
            city_list = []
            for i in range(0, 12):
                city_list.append(data.split(", ")[i])

        return city_list
    elif mode == 'w':
        with open(os.path.join('Assets' , 'City_files', filename), 'w') as file:
            for i in range(0, 12):
                file.writelines([city_list[i], ", "])


def open_player_file(mode, filename):
    global player_list

    if mode == 'r':
        with open(os.path.join('Assets' , 'Properties', filename), 'r') as file:
            data = file.read()
            player_list = []
            for i in range(0, 2):
                player_list.append(data.split(", ")[i])

        return player_list
    elif mode == 'w':
        with open(os.path.join('Assets' , 'Properties', filename), 'w') as file:
            for i in range(0, 2):
                file.writelines([player_list[i], ", "])


def quit_game(event):
    if event.type == pygame.QUIT:

        for color in colors:
            global player_list
            player_list = open_player_file('r', f"{color}.txt")

            player_list[1] = "0"
            
            if color != "bank":
                player_list[0] = "0"
            elif color == "bank":
                player_list[0] = "26"

            open_player_file('w', f"{color}.txt")

        for city in cities_list:
            global city_list

            city_list = open_city_file( 'r', f"{city}.txt")

            city_list[1] = "False"
            city_list[2] = "Null"
            city_list[11] = "0"

            open_city_file( 'w', f"{city}.txt")

        running = False
        pygame.quit()


def console_write(text, delay = 500, color = BLACK):
    text_draw = FONT_s.render(text, True, WHITE, color)
    
    WINDOW.blit(text_draw, [WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE/2 - text_draw.get_width()/2, WINDOW.get_height()/2 - text_draw.get_height()/2])

    pygame.display.update()
    pygame.time.delay(delay)


def draw_gui():
    global click_x, click_y, red_net_worth, green_net_worth, blue_net_worth, yellow_net_worth

    pygame.draw.line(WINDOW, WHITE, (WINDOW.get_width() * 0.75, 0), (WINDOW.get_width() * 0.75, WINDOW.get_height()))

    #Drawing the outer border according the players turn
    if red_turn:
        pygame.draw.rect(WINDOW, RED, [0, 0, WINDOW.get_width(), WINDOW.get_height()], 3)
    elif green_turn:
        pygame.draw.rect(WINDOW, GREEN, [0, 0, WINDOW.get_width(), WINDOW.get_height()], 3)
    elif blue_turn:
        pygame.draw.rect(WINDOW, BLUE, [0, 0, WINDOW.get_width(), WINDOW.get_height()], 3)
    elif yellow_turn:
        pygame.draw.rect(WINDOW, YELLOW, [0, 0, WINDOW.get_width(), WINDOW.get_height()], 3)

    end_start = WINDOW.get_height() - 120
    end_rect = pygame.draw.rect(WINDOW, BLACK, [10, end_start, 250, 80], 3)
    re_size_image("end_game.png", 250, 80, 10, end_start)

    if end_rect.collidepoint(click_x, click_y):
        print("Game ended")

        for city in cities_list:
            global city_list

            city_list = open_city_file( 'r', f"{city}.txt")
            check_owner = city_list[2]
            city_list[3] = int(city_list[3])

            if check_owner == 'red':
                red_net_worth += city_list[3]
                print("Red" ,red_net_worth)
            elif check_owner == 'green':
                green_net_worth += city_list[3]
                print("Green" ,green_net_worth)
            elif check_owner == 'blue':
                blue_net_worth += city_list[3]
                print("Blue" ,blue_net_worth)
            elif check_owner == 'yellow':
                yellow_net_worth += city_list[3]
                print("Yellow" ,yellow_net_worth)
            
        max_number = max(red_net_worth, green_net_worth, blue_net_worth, yellow_net_worth)

        if max_number == red_net_worth:
            print("red")
            ending_screen("red", red_net_worth)
        elif max_number == green_net_worth:
            print("green")
            ending_screen("green", green_net_worth)
        elif max_number == blue_net_worth:
            print("blue")
            ending_screen("blue", blue_net_worth)
        elif max_number == yellow_net_worth:
            print("yellow")
            ending_screen("yellow", yellow_net_worth)


def draw_dice():
    global click_x, click_y, random_number1, random_number2, clicked
    dice_offset = 100
    dice_offset2 = 110 + DICE_SIZE
    DICE_POS_X = WINDOW.get_width() * 0.75 - DICE_SIZE/2 + dice_offset - dice_offset/3
    DICE_POS_Y = WINDOW.get_height() * 0.1 - DICE_SIZE/2

    dice_rect = pygame.draw.rect(WINDOW, WHITE, [DICE_POS_X + dice_offset, DICE_POS_Y + DICE_SIZE + 10, DICE_SIZE*2 + (dice_offset2 - DICE_SIZE*2), DICE_SIZE/2], 3)
    roll_dice_text = FONT_s.render("Roll Dice", True, WHITE)
    WINDOW.blit(roll_dice_text, [(DICE_POS_X + dice_offset) + (DICE_SIZE*2 + (dice_offset2 - DICE_SIZE*2)) / 2 - roll_dice_text.get_width()/2, DICE_POS_Y + DICE_SIZE + 15])

    if dice_rect.collidepoint(click_x, click_y) and clicked == False:
        random_number1 = random.randint(1, 6)
        random_number2 = random.randint(1, 6)
        print(random_number1 + random_number2)
        
        clicked = True
        
    if random_number2 == 1:
        WINDOW.blit(Dice1, [DICE_POS_X + dice_offset, DICE_POS_Y])
    elif random_number2 == 2:
        WINDOW.blit(Dice2, [DICE_POS_X + dice_offset, DICE_POS_Y])
    elif random_number2 == 3:
        WINDOW.blit(Dice3, [DICE_POS_X + dice_offset, DICE_POS_Y])
    elif random_number2 == 4:
        WINDOW.blit(Dice4, [DICE_POS_X + dice_offset, DICE_POS_Y])
    elif random_number2 == 5:
        WINDOW.blit(Dice5, [DICE_POS_X + dice_offset, DICE_POS_Y])
    elif random_number2 == 6:
        WINDOW.blit(Dice6, [DICE_POS_X + dice_offset, DICE_POS_Y])

    if random_number1 == 1:
        WINDOW.blit(Dice1, [DICE_POS_X + dice_offset2, DICE_POS_Y])
    elif random_number1 == 2:
        WINDOW.blit(Dice2, [DICE_POS_X + dice_offset2, DICE_POS_Y])
    elif random_number1 == 3:
        WINDOW.blit(Dice3, [DICE_POS_X + dice_offset2, DICE_POS_Y])
    elif random_number1 == 4:
        WINDOW.blit(Dice4, [DICE_POS_X + dice_offset2, DICE_POS_Y])
    elif random_number1 == 5:
        WINDOW.blit(Dice5, [DICE_POS_X + dice_offset2, DICE_POS_Y])
    elif random_number1 == 6:
        WINDOW.blit(Dice6, [DICE_POS_X + dice_offset2, DICE_POS_Y])


def draw_players(temp_x, temp_y):

    if red_turn:
        pygame.draw.circle(WINDOW, BLACK, [temp_x, temp_y], 20)
        pygame.draw.circle(WINDOW, RED, [temp_x, temp_y], 15)
    elif green_turn:
        pygame.draw.circle(WINDOW, BLACK, [temp_x, temp_y], 20)
        pygame.draw.circle(WINDOW, GREEN, [temp_x, temp_y], 15)
    elif blue_turn:
        pygame.draw.circle(WINDOW, BLACK, [temp_x, temp_y], 20)
        pygame.draw.circle(WINDOW, BLUE, [temp_x, temp_y], 15)
    elif yellow_turn:
        pygame.draw.circle(WINDOW, BLACK, [temp_x, temp_y], 20)
        pygame.draw.circle(WINDOW, YELLOW, [temp_x, temp_y], 15)
        
    # pygame.draw.rect(WINDOW, WHITE, [WINDOW.get_width() * 0.75, WINDOW.get_height() * 0.25, 100, 500], 3)


def draw_game_card(change = False):
    global smallsize
    global rect_end
    FONT_s25 = pygame.font.SysFont('comicsans', smallsize)

    global buy_box_height
    global buy_box_width

    buy_box_height = (WINDOW.get_height() - 10) - (WINDOW.get_height() - 100) - 10 
    buy_box_width = ((WINDOW.get_width() - 10) - (WINDOW.get_width() * 0.75 + 10)) / 2

    draw_rectangle(WINDOW.get_width() * 0.75, WINDOW.get_height() * 0.28, WINDOW.get_width() - 10 , WINDOW.get_height() - 10)
    # draw_rectangle(WINDOW.get_width() * 0.75 + 10,  WINDOW.get_height() - 100, WINDOW.get_width() * 0.75 - 10 + (WINDOW.get_width() - 10 - WINDOW.get_width() * 0.75 + 10)/2,  WINDOW.get_height() - 20 )
    # draw_rectangle(WINDOW.get_width() * 0.75 + (WINDOW.get_width() - 10 - WINDOW.get_width() * 0.75 + 10)/2,  WINDOW.get_height() - 100, WINDOW.get_width() - 20 ,  WINDOW.get_height() - 20 )

    if change == True:
        re_size_image('pay_rent.png', buy_box_width, buy_box_height, WINDOW.get_width() * 0.75 + 5, WINDOW.get_height() - 100)
    else:
        re_size_image('buy_button.png', buy_box_width, buy_box_height, WINDOW.get_width() * 0.75 + 5, WINDOW.get_height() - 100)
        re_size_image('cancel_button.png', buy_box_width - 5, buy_box_height, WINDOW.get_width() * 0.75 + (WINDOW.get_width() - 10 - WINDOW.get_width() * 0.75 + 10)/2, WINDOW.get_height() - 100)

    city_name = FONT_s.render(city_list[0], True, WHITE)
    WINDOW.blit(city_name, [((WINDOW.get_width() * 0.75 )+ (WINDOW.get_width() - (WINDOW.get_width() * 0.75))/2) - city_name.get_width()/2,  WINDOW.get_height() * 0.28 + 10])

    city_purchasing_cost = FONT_s.render(city_list[3], True, WHITE)
    WINDOW.blit(city_purchasing_cost, [((WINDOW.get_width() * 0.75 )+ (WINDOW.get_width() - (WINDOW.get_width() * 0.75))/2) - city_purchasing_cost.get_width()/2,  WINDOW.get_height() * 0.28 + 10 + city_name.get_height()])

    
    draw_rectangle(WINDOW.get_width() * 0.75 + 10, WINDOW.get_height() * 0.28 + (city_name.get_height() + city_purchasing_cost.get_height()) + 20, WINDOW.get_width() - 20, rect_end)
    # re_size_image_city(f"{city_list[0].lower()}_img.png",WINDOW.get_width() - 20 - WINDOW.get_width() * 0.75 + 10,rect_end -  WINDOW.get_height() * 0.28 + (city_name.get_height() + city_purchasing_cost.get_height()) + 20,  WINDOW.get_width() * 0.75 + 10, WINDOW.get_height() * 0.28 + (city_name.get_height() + city_purchasing_cost.get_height()) + 20)

    city_rent = FONT_s25.render(f"Rent: {city_list[4]}", True, WHITE)
    WINDOW.blit(city_rent, [WINDOW.get_width() * 0.75 + 10, rect_end + 10])

    city_house1 = FONT_s25.render(f"House 1: {city_list[5]}", True, WHITE)
    WINDOW.blit(city_house1, [WINDOW.get_width() * 0.75 + 10, rect_end + 10 + (city_rent.get_height())])

    city_house2 = FONT_s25.render(f"House 2: {city_list[6]}", True, WHITE)
    WINDOW.blit(city_house2, [WINDOW.get_width() * 0.75 + 10, rect_end + 10 + (city_rent.get_height() + city_house1.get_height())])

    city_house3 = FONT_s25.render(f"House 3: {city_list[7]}", True, WHITE)
    WINDOW.blit(city_house3, [WINDOW.get_width() * 0.75 + 10, rect_end + 10 + (city_rent.get_height() + city_house1.get_height() + city_house2.get_height())])

    city_hotel = FONT_s25.render(f"Hotel: {city_list[8]}", True, WHITE)
    WINDOW.blit(city_hotel, [WINDOW.get_width() * 0.75 + 10, rect_end + 10 + (city_rent.get_height() + city_house1.get_height() + city_house2.get_height() + city_house3.get_height())])

    city_house_cost = FONT_s25.render(f"House & Hotel cost: {city_list[9]}", True, WHITE)
    WINDOW.blit(city_house_cost, [WINDOW.get_width() * 0.75 + 10, rect_end + 10 + (city_rent.get_height() + city_house1.get_height() + city_house2.get_height() + city_house3.get_height()*3)])

    mortgage = FONT_s25.render(f"Property Mortgage: {city_list[10]}", True, WHITE)
    WINDOW.blit(mortgage, [WINDOW.get_width() * 0.75 + 10, rect_end + 10 + (city_rent.get_height() + city_house1.get_height() + city_house2.get_height() + city_house3.get_height()*4)])

    if rect_end + 10 + (city_rent.get_height() + city_house1.get_height() + city_house2.get_height() + city_house3.get_height()*4) > WINDOW.get_height() - 100:
        rect_end -= (MID_RECT_WIDTH - 25) 
        smallsize = 20

    pygame.display.update()


def final_draw():
    pygame.draw.circle(WINDOW, BLACK, [red_x, red_y], 20)
    pygame.draw.circle(WINDOW, RED, [red_x, red_y], 15)

    pygame.draw.circle(WINDOW, BLACK, [green_x, green_y], 20)
    pygame.draw.circle(WINDOW, GREEN, [green_x, green_y], 15)

    pygame.draw.circle(WINDOW, BLACK, [blue_x, blue_y], 20)
    pygame.draw.circle(WINDOW, BLUE, [blue_x, blue_y], 15)

    pygame.draw.circle(WINDOW, BLACK, [yellow_x, yellow_y], 20)
    pygame.draw.circle(WINDOW, YELLOW, [yellow_x, yellow_y], 15)


def buy_funtion():

    global red_properties_owned, green_properties_owned, blue_properties_owned, yellow_properties_owned
    global player_list, city_list


    if red_turn:
        red_properties_owned += 1
        # open_file('red.txt', red_properties_owned)

        player_list = open_player_file('r', "red.txt")
        player_list[0] = str(red_properties_owned)

        player_list[1] = int(player_list[1])
        player_list[1] -= int(city_list[3])
        player_list[1] = str(player_list[1])

        open_player_file('w', "red.txt")

        print("red properties are ", player_list[0])
    elif green_turn:
        green_properties_owned += 1
        # open_file('green.txt', green_properties_owned)
                
        player_list = open_player_file('r', "green.txt")
        player_list[0] = str(green_properties_owned)

        player_list[1] = int(player_list[1])
        player_list[1] -= int(city_list[3])
        player_list[1] = str(player_list[1])

        open_player_file('w', "green.txt")

        print("green properties are ", player_list[0])
    elif blue_turn:
        blue_properties_owned += 1
        # open_file('blue.txt', blue_properties_owned)
                        
        player_list = open_player_file('r', "blue.txt")
        player_list[0] = str(blue_properties_owned)

        player_list[1] = int(player_list[1])
        player_list[1] -= int(city_list[3])
        player_list[1] = str(player_list[1])

        open_player_file('w', "blue.txt")

        print("blue properties are ", player_list[0])
    elif yellow_turn:
        yellow_properties_owned += 1
        # open_file('yellow.txt', yellow_properties_owned)
                                
        player_list = open_player_file('r', "yellow.txt")
        player_list[0] = str(yellow_properties_owned)

        player_list[1] = int(player_list[1])
        player_list[1] -= int(city_list[3])
        player_list[1] = str(player_list[1])

        open_player_file('w', "yellow.txt")

        print("yellow properties are ", player_list[0])
    

    #Adding money to bank and subtracting its no. of properties
    player_list = open_player_file('r', "bank.txt")
    player_list[0] = int(player_list[0])
    player_list[0] -= 1
    player_list[0] = str(player_list[0])

    player_list[1] = int(player_list[1])
    player_list[1] += int(city_list[3])
    player_list[1] = str(player_list[1])

    open_player_file('w', "bank.txt")
    #opening a file with the city name and then making the player whose turn is on its owner
     

def the_transaction(property_sold, click_x, click_y, city_name_var):

    print(property_sold)

    draw_game_card()

    clicked = False

    while property_sold == "False":
        if (click_x >= WINDOW.get_width() * 0.75 + 5 and click_x <= WINDOW.get_width() * 0.75 + 5 + buy_box_width) and (click_y >= WINDOW.get_height() - 100 and click_y <= WINDOW.get_height() - 100 + buy_box_height):
            print("CLicked on buy")
            console_write("Clicked on buy")

            property_sold = True
            bool_property_sold = True

            global city_list
            city_list[1] = "True"

            if red_turn:
                city_list[2] = "red"
            elif green_turn:
                city_list[2] = "green"    
            elif blue_turn:
                city_list[2] = "blue"
            elif yellow_turn:
                city_list[2] = "yellow"
            
            
            click_x = 0
            click_y = 0

            clicked = True

            buy_funtion()

            return bool_property_sold

        elif (click_x >=  WINDOW.get_width() * 0.75 + (WINDOW.get_width() - 10 - WINDOW.get_width() * 0.75 + 10)/2 and click_x <= WINDOW.get_width() - 20) and (click_y >= WINDOW.get_height() - 100 and click_y <= WINDOW.get_height() - 100 + buy_box_height):
            print("CLicked on Cancel")
            console_write("Clicked on Cancel")
            property_sold = True
            bool_property_sold = False
            click_x = 0
            click_y = 0

            clicked = True

            return bool_property_sold
        else:
            for event in pygame.event.get():
                quit_game(event)

                if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                    click_x = event.pos[0]
                    click_y = event.pos[1]

                    print(click_x, " ", click_y)
    else:
        check_owner = city_list[2]
        global player_list, player_turn
        click_x1 = 0
        click_y2 = 0


        paying = True
        pay_rent = pygame.draw.rect(WINDOW, BLACK, [WINDOW.get_width() * 0.75 + 5, WINDOW.get_height() - 100, buy_box_width, buy_box_height ])

        draw_game_card(change=True) 

        while paying:
            if check_owner != player_turn:
                #Adding the rent to the players property
                console_write(f"City is already purchased, pay rent, {city_list[4]}")

                if pay_rent.collidepoint(click_x1, click_y2):
                    player_list = open_player_file('r', f"{check_owner}.txt")
                    print("City is already purchased, pay rent", city_list[4])

                    player_list[1] = int(player_list[1])
                    print(f"{check_owner}'s property ", player_list[1])
                    player_list[1] += int(city_list[4])
                    print(player_list[1])
                    player_list[1] = str(player_list[1])

                    open_player_file('w', f"{check_owner}.txt")

                    #Subtracting the rent from the players property
                    player_list = open_player_file('r', f"{player_turn}.txt")

                    player_list[1] = int(player_list[1])
                    print(f"{player_turn} has landed ", player_list[1])

                    player_list[1] -= int(city_list[4])
                    print(player_list[1])
                    player_list[1] = str(player_list[1])

                    open_player_file('w', f"{player_turn}.txt")

                    paying = False
            else:
                paying = False

            for event in pygame.event.get():
                quit_game(event)

                if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                    click_x1 = event.pos[0]
                    click_y2 = event.pos[1]

                    print(click_x1, " ", click_y2)


def player_movement(random_number1, random_number2, temp_x, temp_y):
    t = random_number1 + random_number2
    temp_x = int(temp_x)
    temp_y = int(temp_y)

    while (t > 0):
        
        if temp_x > left_line_x and temp_y == bottom_line_y:
            temp_x -= MID_RECT_WIDTH
            if temp_x < left_line_x:
                temp_x = left_line_x
            #     temp_y -=   MID_RECT_WIDTH
        elif (temp_x == left_line_x) and temp_y > top_line_y:
            temp_y -= MID_RECT_WIDTH
            if temp_y < top_line_y:
                temp_y = top_line_y
            #     temp_x += MID_RECT_WIDTH
        elif temp_y == top_line_y and temp_x < right_line_x:
            temp_x += MID_RECT_WIDTH
            if temp_x > right_line_x:
                temp_x = right_line_x
            #     temp_y += MID_RECT_WIDTH
        elif temp_x == right_line_x and temp_y < bottom_line_y:
            temp_y += MID_RECT_WIDTH
            if temp_y > bottom_line_y:
                temp_y = bottom_line_y
            #     temp_x -= MID_RECT_WIDTH


        # print(t, ":-  (", temp_x, ", ", temp_y, ") ", end="")
        t -= 1

        p_start = 0

        if red_turn:
            global red_start
            red_start += 1

            if red_start == 36:
                print("Player passed from start, p_value zeroed")
                unique_citis("start")
                red_start = 0

            p_start = red_start
        elif green_turn:
            global green_start
            green_start += 1

            if green_start == 36:
                print("Player passed from start, p_value zeroed")
                unique_citis("start")
                green_start = 0

            p_start = green_start
        elif blue_turn  :
            global blue_start
            blue_start += 1

            if blue_start == 36:
                print("Player passed from start, p_value zeroed")
                unique_citis("start")
                blue_start = 0

            p_start = blue_start
        elif yellow_turn:
            global yellow_start
            yellow_start += 1

            if yellow_start == 36:
                print("Player passed from start, p_value zeroed")
                unique_citis("start")
                yellow_start = 0

            p_start = yellow_start
            
    
        if red_turn:
            global red_x, red_y
            red_x = temp_x
            red_y = temp_y
        elif green_turn:
            global green_x, green_y
            green_x = temp_x
            green_y = temp_y
        elif blue_turn:
            global blue_x, blue_y
            blue_x = temp_x
            blue_y = temp_y
        elif yellow_turn:
            global yellow_x, yellow_y
            yellow_x = temp_x
            yellow_y = temp_y
            
        
        WINDOW.fill(BLACK)
        draw_dice()
        draw_players(temp_x, temp_y)
        board.board_draw(WINDOW)
        final_draw()

        pygame.display.update()

        pygame.time.delay(200)
    
    return p_start


def bank_player_transaction(amount):
    global player_list, player_turn
    player_list = open_player_file('r', f"{player_turn}.txt")

    player_list[1] = int(player_list[1])
    player_list[1] += amount
    player_list[1] = str(player_list[1])

    open_player_file('w', f"{player_turn}.txt")

    player_list = open_player_file('r', "bank.txt")

    player_list[1] = int(player_list[1])
    player_list[1] -= amount
    player_list[1] = str(player_list[1])

    open_player_file('w', "bank.txt")


def unique_citis(city, total_random=0):
    global player_list, player_turn, random_number1, random_number2
    random_number1 = 12 
    random_number2 = 0


    if city == "jail":
        print("PLayer landed in jail, roll dice 3 times")
        console_write("Player landed in jail, roll dice 3 times")
        rolled = 0
        while rolled < 3:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE :

                        random_number1 = random.randint(1, 6)
                        random_number2 = random.randint(1, 6)
                        print(random_number1 + random_number2)
                        rolled += 1

            draw_dice()
            pygame.display.update()

            if random_number1 == random_number2:
                print("Player got out of jail")
                break

    elif city == "club house":
        print("Player landed in club house, player pays everyone 100 and skips next turn")
        console_write("Player landed in club house, player pays everyone 100 and skips next turn", 1000)

        player_list = open_player_file('r', f"{player_turn}.txt")
        player_list[1] = int(player_list[1])
        player_list[1] -= 400
        player_list[1] = str(player_list[1])

        open_player_file('w', f"{player_turn}.txt")

        for color in colors:
            if color == f"{player_turn}":
                continue

            player_list = open_player_file('r', f"{color}.txt")
            player_list[1] = int(player_list[1])
            player_list[1] += 100
            player_list[1] = str(player_list[1])

            open_player_file('w', f"{color}.txt")

    elif city == "rest house":
        print("Player landed in club house, everyones pays player 100 and player skips next turn")
        console_write("Player landed in club house, everyones pays player 100 and player skips next turn", 1000)


        player_list = open_player_file('r', f"{player_turn}.txt")
        player_list[1] = int(player_list[1])
        player_list[1] += 400
        player_list[1] = str(player_list[1])

        open_player_file('w', f"{player_turn}.txt")

        for color in colors:
            if color == f"{player_turn}":
                continue

            player_list = open_player_file('r', f"{color}.txt")
            player_list[1] = int(player_list[1])
            player_list[1] -= 100
            player_list[1] = str(player_list[1])

            open_player_file('w', f"{color}.txt")

    elif city == "start":
        print("Player gets 1500 from bank")
        console_write("Player has passed 'start', gets 1500 from bank", 750)

        player_list = open_player_file('r', f"{player_turn}.txt")
        player_list[1] = int(player_list[1])
        player_list[1] += 1500
        player_list[1] = str(player_list[1])

        open_player_file('w', f"{player_turn}.txt")

        player_list = open_player_file('r', "bank.txt")

        player_list[1] = int(player_list[1])
        player_list[1] -= 1500
        player_list[1] = str(player_list[1])

        open_player_file('w', "bank.txt")

    elif city == "chance":
        if total_random == 2:
            print(" Loss in Share Market Rs. 2000")
            console_write(" Loss in Share Market Rs. 2000", 1000)
            bank_player_transaction(-2000)
        elif total_random == 3:
            print("Lottery prize Rs. 2500")
            console_write("Lottery prize Rs. 2500", 1000)
            bank_player_transaction(2500)
        elif total_random == 4:
            print("Fine for accident due to driving under the liquor influence, Rs. 1500")
            console_write("Fine for accident due to driving under the liquor influence, Rs. 1500", 1000)
            bank_player_transaction(-1500)
        elif total_random == 5:
            print("You have won the third prize of Rs. 1000 in a TV singing show")
            console_write("You have won the third prize of Rs. 1000 in a TV singing show", 1000)
            bank_player_transaction(1000)
        elif total_random == 6:
            print("House Repairing Rs. 1500")
            console_write("House Repairing Rs. 1500", 1000)
            bank_player_transaction(-1500)
        elif total_random == 7:
            print("You have won a Jackpot of Rs. 2000")
            console_write("You have won a Jackpot of Rs. 2000", 1000)
            bank_player_transaction(2000)
        elif total_random == 8:
            print("Loss due to fire in godown. Rs. 3000")
            console_write("Loss due to fire in godown. Rs. 3000", 1000)
            bank_player_transaction(-3000)
        elif total_random == 9:
            print("Go back to Mumbai. if you have to pass starting point. collect Rs 1500.00 and go to Agra")
            console_write("Go back to Mumbai. if you have to pass starting point. collect Rs 1500.00 and go to Agra")
        elif total_random == 10:
            print("Go to Prison")
            console_write("Go to Prison")
        elif total_random == 11:
            print("Best Performance in Export, Rs. 3000")
            console_write("Best Performance in Export, Rs. 3000", 1000)
            bank_player_transaction(3000)
        elif total_random == 12:
            print("Go to Rest House, you cannot play the next turn")
            console_write("Go to Rest House, you cannot play the next turn", 1000)

    elif city == "community":
        if total_random == 2:
            print("it is your birthday Collect from each player Rs. 500")
            console_write("it is your birthday Collect from each player Rs. 500", 1000)
        elif total_random == 3:
            print("Go to prison")
        elif total_random == 4:
            print("First prze in reality TV show Rs. 2500")
            console_write("First prze in reality TV show Rs. 2500", 1000)
            bank_player_transaction(2500)
        elif total_random == 5:
            print("Faulty Electrical Connection in your house led to a short circuit Pay Rs. 1000 as fine.")
            console_write("Faulty Electrical Connection in your house led to a short circuit Pay Rs. 1000 as fine.", 1000)
            bank_player_transaction(-1500)
        elif total_random == 6:
            print("Income tax refund Rs. 2000")
            console_write("Income tax refund Rs. 2000", 1000)
            bank_player_transaction(2000)
        elif total_random == 7:
            print("Marriage celebration, Rs. 2000")
            console_write("Marriage celebration, Rs. 2000", 1000)
            bank_player_transaction(-2000)
        elif total_random == 8:
            print("Go to Rest House, you cannot play the next turn")
        elif total_random == 9:
            print("Make general repair on all your properties \n Each house pay Rs 100 \n Each hotel pay Rs. 200")
            console_write("Make general repair on all your properties \n Each house pay Rs 100 \n Each hotel pay Rs. 200", 1000)
        elif total_random == 10:
            print("Receive interest on share investment, Rs. 1500")
            console_write("Receive interest on share investment, Rs. 1500", 1000)
            bank_player_transaction(1500)
        elif total_random == 11:
            print("Pay insurance premium. Rs. 1500")
            console_write("Pay insurance premium. Rs. 1500", 1000)
            bank_player_transaction(-1500)
        elif total_random == 12:
            print("Sale of Stocks, Collect Rs. 3000")
            console_write("Sale of Stocks, Collect Rs. 3000", 1000)
            bank_player_transaction(3000)
    

def city_info(pos, click_x, click_y):
    global city_list, total_random
    global city_name_var

    if pos == 1: #MUMBAI 
        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'mumbai.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)

        #checks wether is the property is sold or not, if true it writes its new owner on the file, if false it does nothing
        if bool_var:
            open_city_file('w', 'mumbai.txt')   

    elif pos == 2: #Railways
        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'railways.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'railways.txt')   

    elif pos == 3: # Pune
        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'pune.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'pune.txt')   

    elif pos == 4:#Aurangabad
        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'aurangabad.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'aurangabad.txt')  

    elif pos == 5:#income tax
        print("Player landed at income tax")
        #Calling the calculate tax function

    elif pos == 6:#electric and water co
        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'electric.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)

        if bool_var:
            open_city_file('w', 'electric.txt')   


    elif pos == 7:#Chance
        print("Player landed in Chance")
        unique_citis("chance", total_random)
        #Calling the chance fiunction

    elif pos == 8:#Roadways
        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'roadways.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'roadways.txt')  
        
    elif pos == 9:#Jail
        print("Player landed in JAIL")
        unique_citis("jail")
        #Calling the jail function

    elif pos == 10:#Jaipur
        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'jaipur.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
                
        if bool_var:
            open_city_file('w', 'jaipur.txt')  

    elif pos == 11:#Udaipur

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'udaipur.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
                        
        if bool_var:
            open_city_file('w', 'udaipur.txt')  

    elif pos == 12:#Waterways

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'waterways.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)

        if bool_var:
            open_city_file('w', 'waterways.txt')  

    elif pos == 13:#Bikaner

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'bikaner.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'bikaner.txt')  

    elif pos == 14:#mysore

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'mysore.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
                
        if bool_var:
            open_city_file('w', 'mysore.txt')  

    elif pos == 15:#Kolkatta

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'kolkatta.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
 
        if bool_var:
            open_city_file('w', 'kolkatta.txt') 

    elif pos == 16:#Community chest
        print("Player landed in community chest")
        unique_citis("community", total_random)

    elif pos == 17:#Guwahati

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'guwahati.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)

        if bool_var:
            open_city_file('w', 'guwahati.txt') 

    elif pos == 18:#Club
        print("Player landed in CLUB")
        unique_citis("club house")

    elif pos == 19:#Chennai

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'chennai.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'chennai.txt') 

    elif pos == 20:#Chance
        print("Player landed in Chance")
        unique_citis("chance", total_random)

    elif pos == 21:#Hydrabad

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'hydrabad.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'hydrabad.txt') 

    elif pos == 22:#Cochin

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'cochin.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'cochin.txt') 

    elif pos == 23:#Varanasi

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'varanasi.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'varanasi.txt') 

    elif pos == 24:#Wealth Tax
        print("Player landed in wealth tax")

    elif pos == 25:#Agra

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'agra.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'agra.txt') 

    elif pos == 26:#Shimla  

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'shimla.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'shimla.txt') 

    elif pos == 27:#Rest House
        print("Player landed in REST HOUSE")
        unique_citis("rest house")

    elif pos == 28:#Goa

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'goa.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'goa.txt') 

    elif pos == 29:#Community Chest
        print("Player landed in community chest")
        unique_citis("community", total_random)

    elif pos == 30:#New Delhi

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'newdelhi.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'newdelhi.txt') 

    elif pos == 31:#Lakshadweep

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'lakshadweep.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'lakshadweep.txt') 

    elif pos == 32:#Amritsar

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'amritsar.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'amritsar.txt') 

    elif pos == 33:#Darjeeling

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'darjeling.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'darjeling.txt') 

    elif pos == 34:#Air ways

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'airways.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'airways.txt') 

    elif pos == 35:#Ahmeadabad

        print("Player landed in the city: " + str(pos))

        city_list = open_city_file('r', 'ahmedabad.txt')
        city_name_var = city_list[0]
        console_write(f"Player has landed in the city: {city_name_var}", 1000)
        bool_var = the_transaction(city_list[1], click_x, click_y, city_name_var)
        
        if bool_var:
            open_city_file('w', 'ahmedabad.txt') 

    elif pos == 36:#Start
        print("Player landed in START, p_value zeroed")


def opening_screen():
    click_x = 0
    click_y = 0

    opnening_running = True
    while opnening_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                opnening_running = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

            if event.type == pygame.MOUSEBUTTONDOWN:
            #    print(event)
               click_x = event.pos[0]
               click_y = event.pos[1]

               print(click_x, " ", click_y)


        # WINDOW.blit(BACKGROUND_IMAGE, [0,0])
        WINDOW.fill(BLACK)

        logo_width = 700

        button_width = 300  
        button_height = WINDOW.get_height() / 10

        logo_rect = pygame.draw.rect(WINDOW, BLACK, [WINDOW.get_width() * 0.5 - logo_width/2, WINDOW.get_height() * 0.1, logo_width, button_height], 3)
        re_size_image("logo.png", logo_width, button_height + 50, WINDOW.get_width() * 0.5 - logo_width/2, WINDOW.get_height() * 0.1)

        sart_rect = pygame.draw.rect(WINDOW, BLACK, [WINDOW.get_width() * 0.5 - button_width/2 , WINDOW.get_height() * 0.32, button_width, button_height], 3)
        re_size_image("start_button.png", button_width, button_height, WINDOW.get_width() * 0.5 - button_width/2, WINDOW.get_height() * 0.32)

        how_rect = pygame.draw.rect(WINDOW, BLACK, [WINDOW.get_width() * 0.5 - button_width/2 , WINDOW.get_height() * 0.32 + button_height + 20, button_width, button_height], 3)
        re_size_image("how to play.png", button_width, button_height, WINDOW.get_width() * 0.5 - button_width/2, WINDOW.get_height() * 0.32 + button_height + 20)
        
        quit_rect = pygame.draw.rect(WINDOW, BLACK, [WINDOW.get_width() * 0.5 - button_width/2 , WINDOW.get_height() * 0.32 + button_height*2 + 20*2, button_width, button_height], 3)
        re_size_image("quit_button.png", button_width, button_height, WINDOW.get_width() * 0.5 - button_width/2, WINDOW.get_height() * 0.32 + button_height*2 + 20*2)



        if sart_rect.collidepoint(click_x, click_y):
            main()
        elif how_rect.collidepoint(click_x, click_y):
            #How to play function
            pass
        elif quit_rect.collidepoint(click_x, click_y):
            quit_game()



        pygame.display.update()
        clock.tick(60)


def ending_screen(player, net_worth):
    global player_list, red_net_worth, green_net_worth, blue_net_worth, yellow_net_worth

    click_x = 0
    click_y = 0

    opnening_running = True
    while opnening_running:
        for event in pygame.event.get():
            quit_game(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
            #    print(event)
               click_x = event.pos[0]
               click_y = event.pos[1]

               print(click_x, " ", click_y)
            
        player_list = open_player_file('r', f"{player}.txt")
        player_list[1] = int(player_list[1])
        final_worth = player_list[1] + net_worth


        # WINDOW.blit(BACKGROUND_IMAGE, [0,0])
        WINDOW.fill(BLACK)

        logo_width = 700

        button_width = 300  
        button_height = WINDOW.get_height() / 10

        logo_rect = pygame.draw.rect(WINDOW, BLACK, [WINDOW.get_width() * 0.5 - logo_width/2, WINDOW.get_height() * 0.1, logo_width, button_height], 3)
        re_size_image("logo.png", logo_width, button_height + 50, WINDOW.get_width() * 0.5 - logo_width/2, WINDOW.get_height() * 0.1)


        players_properties = FONT.render(f"{player.capitalize()} has {player_list[0]} properties", True, WHITE)
        WINDOW.blit(players_properties, [WINDOW.get_width()/2 - players_properties.get_width()/2, WINDOW.get_height() * 0.1 + button_height + 50 ])

        players_money = FONT.render(f"{player.capitalize()} has {player_list[1]} amount of money left", True, WHITE)
        WINDOW.blit(players_money, [WINDOW.get_width()/2 - players_money.get_width()/2, WINDOW.get_height() * 0.1 + button_height + 50  + players_properties.get_height()])

        players_net_worth = FONT.render(f"{player.capitalize()} has {net_worth} worth of properties", True, WHITE)
        WINDOW.blit(players_net_worth, [WINDOW.get_width()/2 - players_net_worth.get_width()/2, WINDOW.get_height() * 0.1 + button_height + 50  + players_properties.get_height()*2])

        players_final_net_worth = FONT.render(f"{player.capitalize()}'s final worth is:  {final_worth}", True, WHITE)
        WINDOW.blit(players_final_net_worth, [WINDOW.get_width()/2 - players_final_net_worth.get_width()/2, WINDOW.get_height() * 0.1 + button_height + 50  + players_properties.get_height()*3])

        text = FONT.render(f"{player.capitalize()} IS THE WINNER", True, WHITE, f"{player.upper()}")
        WINDOW.blit(text, [WINDOW.get_width()/2 - text.get_width()/2, WINDOW.get_height() * 0.1 + button_height + 50  + players_properties.get_height() * 4])


        pygame.display.update()
        clock.tick(60)


def main():
    click1 = False
    click2 = False

    cheating = False

    global click_x
    global click_y 

    global red_y, red_x, green_x, green_y, blue_x, blue_y, yellow_x, yellow_y, starting_money, player_list, random_number1, random_number2, clicked

    for color in colors:
            global player_list
            player_list = open_player_file('r', f"{color}.txt")

            player_list[1] = f"{starting_money}"

            open_player_file('w', f"{color}.txt")

    p1 = 0

    running = True
    while running:
        click_x = 0
        click_y = 0
        clock.tick(60)
        WINDOW.fill(BLACK)

        global red_turn, green_turn, blue_turn, yellow_turn
        global player_turn
        if red_turn:
            player_turn = "red"
        elif green_turn:
            player_turn = "green"
        elif blue_turn:
            player_turn = "blue"
        else:
            player_turn = "yellow"

        for event in pygame.event.get():
            quit_game(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    cheating = True

                if event.key == pygame.K_SPACE and clicked == False and cheating == False:

                    random_number1 = random.randint(1, 6)
                    random_number2 = random.randint(1, 6)
                    print(random_number1 + random_number2)
                    
                    clicked = True

                if cheating:
                    if event.key == pygame.K_1 and click1 == False:
                        random_number1 = 1
                        click1 = True
                    elif event.key == pygame.K_2 and click1 == False:
                        random_number1 = 2
                        click1 = True
                    elif event.key == pygame.K_3 and click1 == False:
                        random_number1 = 3
                        click1 = True
                    elif event.key == pygame.K_4 and click1 == False:
                        random_number1 = 4
                        click1 = True
                    elif event.key == pygame.K_5 and click1 == False:
                        random_number1 = 5
                        click1 = True
                    elif event.key == pygame.K_6 and click1 == False:
                        random_number1 = 6
                        click1 = True

                    if event.key == pygame.K_KP_1 and click2 == False:
                        random_number2 = 1
                        click2 = True
                    elif event.key == pygame.K_KP_2 and click2 == False:
                        random_number2 = 2
                        click2 = True
                    elif event.key == pygame.K_KP_3 and click2 == False:
                        random_number2 = 3
                        click2 = True
                    elif event.key == pygame.K_KP_4 and click2 == False:
                        random_number2 = 4
                        click2 = True
                    elif event.key == pygame.K_KP_5 and click2 == False:
                        random_number2 = 5
                        click2 = True
                    elif event.key == pygame.K_KP_6 and click2 == False:
                        random_number2 = 6
                        click2 = True
                    
                    if click2 and click1:
                        clicked = True
                        click1 = False
                        click2 = False
                        cheating = False
                    else:
                        clicked = False

                    print(random_number1 + random_number2)

            if event.type == pygame.MOUSEBUTTONDOWN:
            #    print(event)
               click_x = event.pos[0]
               click_y = event.pos[1]

               print(click_x, " ", click_y)

        draw_dice()

        global total_random    
        total_random = random_number1 + random_number2

        if clicked:
            if red_turn:
                p1 = player_movement(random_number1, random_number2, red_x, red_y)
                city_info(p1, click_x, click_y)
                red_turn = False
                green_turn = True
            elif green_turn:
                p1 = player_movement(random_number1, random_number2, green_x, green_y)
                city_info(p1, click_x, click_y)
                green_turn = False
                blue_turn = True
            elif blue_turn:
                p1 = player_movement(random_number1, random_number2, blue_x, blue_y)
                city_info(p1, click_x, click_y)
                blue_turn = False
                yellow_turn = True
            elif yellow_turn:
                p1 = player_movement(random_number1, random_number2, yellow_x, yellow_y)
                city_info(p1, click_x, click_y)
                yellow_turn = False
                red_turn = True
            
            global city_list
            city_list = []
            player_list = []

            clicked = False



        board.board_draw(WINDOW)
        draw_gui()
        final_draw()


        pygame.display.update()
   
        
    main()

opening_screen()
