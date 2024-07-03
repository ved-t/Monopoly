import sys
import pygame
import os

# import logic 
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Loading the FOnt
bigsize = 55
smallsize = 25

player_list = []
city_list = []

color = WHITE
console_list = []

i = 1

def give_varialbes(WINDOW):
    minus_offset = 10
    BOARD_START_POS = 0.20
    BOARD_SIZE = WINDOW.get_height() - minus_offset

    CORNER_SQ_SIZE = (BOARD_SIZE/12) * 2
    MID_RECT_WIDTH = (BOARD_SIZE/12)
    MID_RECT_HEIGHT = (BOARD_SIZE/12) * 2

    return BOARD_START_POS, BOARD_SIZE, CORNER_SQ_SIZE, MID_RECT_WIDTH, MID_RECT_HEIGHT


def open_file(filename):
    with open(os.path.join('Assets', 'Properties', filename), 'r') as file:
        data = file.read()
        player_list = []
        for i in range(0, 2):
            player_list.append(data.split(", ")[i])

    return player_list


def open_city_file(filename):
    with open(os.path.join('Assets' , 'City_files', filename), 'r') as file:
        data = file.read()
        city_list = []
        for i in range(0, 11):
            city_list.append(data.split(", ")[i])
        
        if city_list[2] == 'red':
            color = RED
        elif city_list[2] == "green":
            color = GREEN
        elif city_list[2] == "blue":
            color = BLUE
        elif city_list[2] == "yellow":
            color = YELLOW
        else:
            color = WHITE

        return color


def console_write(WINDOW, text, MID_RECT_WIDTH):
    global FONT_s, i, console_list
    
    for number in range(1, i+1):
        console_list.append(FONT_s.render(text, True, WHITE))
        WINDOW.blit(console_list[i - 1], [10 * 2, MID_RECT_WIDTH*8 + 30 + console_list[i-1].get_height() * i])
        pygame.display.update()

    i += 1
    
    pygame.display.update()


def board_draw(WINDOW):
    def re_size_image(image_name, img_size_height, img_size_width, pos_x, pos_y):
        image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Business_images', image_name)), (img_size_height, img_size_width))
        WINDOW.blit(image, [pos_x, pos_y])


    global smallsize, color, FONT_s

    FONT = pygame.font.SysFont('comicsans', bigsize)
    FONT_s = pygame.font.SysFont('comicsans', smallsize)

    def draw_rectangle(start_pos_x, start_pos_y, end_pos_x, end_pos_y):
        widht = end_pos_x - start_pos_x
        hight = end_pos_y - start_pos_y
        pygame.draw.rect(WINDOW, WHITE, [start_pos_x, start_pos_y, widht, hight], 3)

    BOARD_START_POS = 0.20
    # minus_offset = WINDOW.get_width() -(BOARD_SIZE + BOARD_START_POS)
    minus_offset = 10

    BOARD_SIZE = WINDOW.get_height() - minus_offset
    if (WINDOW.get_height()) < BOARD_SIZE:
        BOARD_SIZE = WINDOW.get_height() - minus_offset
    elif (WINDOW.get_width() - (WINDOW.get_width() * BOARD_START_POS)) < BOARD_SIZE:
    # elif (WINDOW.get_width() - (WINDOW.get_width() - ((WINDOW.get_width() * BOARD_START_POS) + BOARD_SIZE))) < ((WINDOW.get_width() * BOARD_START_POS) + BOARD_SIZE):
        BOARD_SIZE = (WINDOW.get_width() * (1- BOARD_START_POS)) - minus_offset

    CORNER_SQ_SIZE = (BOARD_SIZE/12) * 2
    MID_RECT_WIDTH = (BOARD_SIZE/12)
    MID_RECT_HEIGHT = (BOARD_SIZE/12) * 2



    #Drawing the square
    pygame.draw.rect(WINDOW, WHITE, [WINDOW.get_width() * BOARD_START_POS, 0, BOARD_SIZE, BOARD_SIZE], 3)
    # re_size_image("Business_game2.jpg", BOARD_SIZE, BOARD_SIZE, WINDOW.get_width() * BOARD_START_POS, 0)

    def draw_images():
        # Corner images
        re_size_image("club_img.png",  CORNER_SQ_SIZE, CORNER_SQ_SIZE, WINDOW.get_width() * BOARD_START_POS, 0)
        re_size_image("rest house.png",  CORNER_SQ_SIZE, CORNER_SQ_SIZE, WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, 0)
        re_size_image("prison_img.png",  CORNER_SQ_SIZE, CORNER_SQ_SIZE, WINDOW.get_width() * BOARD_START_POS, BOARD_SIZE - CORNER_SQ_SIZE)
        re_size_image("start_img.png",  CORNER_SQ_SIZE, CORNER_SQ_SIZE, WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, BOARD_SIZE - CORNER_SQ_SIZE)

        #Topmost line
        re_size_image("chennai_img.png",  MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + CORNER_SQ_SIZE, 0)
        re_size_image("chance_img.png",  MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*3, 0)
        re_size_image("hyderabad_img.png",  MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*4, 0)
        re_size_image("cochin_img.png",  MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*5, 0)
        re_size_image("varanasi_img.png",  MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*6, 0)
        re_size_image("wealth_tax_img.png",  MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*7, 0)
        re_size_image("agra_img.png",  MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*8, 0)
        re_size_image("Shimla_img.png",  MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*9, 0)

        # Bottmost line
        re_size_image("roadways_img.png", MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + CORNER_SQ_SIZE,  BOARD_SIZE - CORNER_SQ_SIZE)
        re_size_image("chance_img.png", MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*3,  BOARD_SIZE - CORNER_SQ_SIZE)
        re_size_image("electric_img.png", MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*4,  BOARD_SIZE - CORNER_SQ_SIZE)
        re_size_image("income tax_img.png", MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*5,  BOARD_SIZE - CORNER_SQ_SIZE)
        re_size_image("aurangabad_img.png", MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*6,  BOARD_SIZE - CORNER_SQ_SIZE)
        re_size_image("pune_img.png", MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*7,  BOARD_SIZE - CORNER_SQ_SIZE)
        re_size_image("railways_img.png", MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*8,  BOARD_SIZE - CORNER_SQ_SIZE)
        re_size_image("mumbai_img.png", MID_RECT_WIDTH, MID_RECT_HEIGHT, WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*9,  BOARD_SIZE - CORNER_SQ_SIZE)

        #leftmost line
        re_size_image("guwahati.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS, CORNER_SQ_SIZE)
        re_size_image("community chest_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*3)
        re_size_image("kolkatta_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH,WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*4)
        re_size_image("mysore_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*5)
        re_size_image("bikaner_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*6)
        re_size_image("waterways_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*7)
        re_size_image("Udaipur_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*8)
        re_size_image("jaipur_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*9)

        # Rightmost line
        re_size_image("goa_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, CORNER_SQ_SIZE)
        re_size_image("community chest_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*3)
        re_size_image("new delhi_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*4)
        re_size_image("lakshadweep_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*5)
        re_size_image("amritsar_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*6)
        re_size_image("darjeeling_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*7)
        re_size_image("airways_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*8)
        re_size_image("ahmedabad_img.png",  MID_RECT_HEIGHT, MID_RECT_WIDTH, WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*9)

    #putting the images
    draw_images()

    # Drawing the corner squares
    #TL
    pygame.draw.rect(WINDOW, WHITE, [WINDOW.get_width() * BOARD_START_POS, 0, CORNER_SQ_SIZE, CORNER_SQ_SIZE], 3)
    #TR
    pygame.draw.rect(WINDOW, WHITE, [WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, 0, CORNER_SQ_SIZE, CORNER_SQ_SIZE], 3)
    #BL
    pygame.draw.rect(WINDOW, WHITE, [WINDOW.get_width() * BOARD_START_POS, BOARD_SIZE - CORNER_SQ_SIZE, CORNER_SQ_SIZE, CORNER_SQ_SIZE], 3)
    #BR
    pygame.draw.rect(WINDOW, WHITE, [WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, BOARD_SIZE - CORNER_SQ_SIZE, CORNER_SQ_SIZE, CORNER_SQ_SIZE], 3)


    #Drawing the rectangle of the top line
    color = open_city_file("chennai.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + CORNER_SQ_SIZE, 0, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    pygame.draw.rect(WINDOW, WHITE, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*3, 0, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    color = open_city_file("hydrabad.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*4, 0, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    color = open_city_file("cochin.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*5, 0, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    color = open_city_file("varanasi.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*6, 0, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    pygame.draw.rect(WINDOW, WHITE, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*7, 0, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    color = open_city_file("agra.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*8, 0, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    color = open_city_file("shimla.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*9, 0, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    #Bottommost line
    color = open_city_file("roadways.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + CORNER_SQ_SIZE,  BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    pygame.draw.rect(WINDOW, WHITE, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*3,  BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    color = open_city_file("electric.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*4,  BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    pygame.draw.rect(WINDOW, WHITE, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*5,  BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    color = open_city_file("aurangabad.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*6,  BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    color = open_city_file("pune.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*7,  BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    color = open_city_file("railways.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*8,  BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)

    color = open_city_file("mumbai.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + MID_RECT_WIDTH*9,  BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH, MID_RECT_HEIGHT], 3)


    #Leftmost line
    color = open_city_file("guwahati.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS, CORNER_SQ_SIZE, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)

    pygame.draw.rect(WINDOW, WHITE, [WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*3, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)
    
    color = open_city_file("kolkatta.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*4, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)

    color = open_city_file("mysore.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*5, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)
    
    color = open_city_file("bikaner.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*6, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)

    color = open_city_file("waterways.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*7, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)

    color = open_city_file("udaipur.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*8, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)

    color = open_city_file("jaipur.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS, MID_RECT_WIDTH*9, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)


    #rightmost line
    color = open_city_file("goa.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, CORNER_SQ_SIZE, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)

    pygame.draw.rect(WINDOW, WHITE, [WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*3, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)

    color = open_city_file("newdelhi.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*4, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)

    color = open_city_file("lakshadweep.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*5, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)

    color = open_city_file("amritsar.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*6, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)

    color = open_city_file("darjeling.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*7, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)

    color = open_city_file("airways.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*8, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)

    color = open_city_file("ahmedabad.txt")
    pygame.draw.rect(WINDOW, color, [WINDOW.get_width() * BOARD_START_POS + BOARD_SIZE - CORNER_SQ_SIZE, MID_RECT_WIDTH*9, MID_RECT_HEIGHT, MID_RECT_WIDTH], 3)


    #Drawing the player icons
    #<<<<<<<<<<<<<<<------------------------------------------>>>>>>>>>>>>>>>>>>>

    player_icon_x = 10
    player_icon_y = 20

    player_icon_size = 100

    if (player_icon_y * 5 + player_icon_size * 4) > WINDOW.get_height()/2:
        player_icon_size = 75


    pygame.draw.rect(WINDOW, WHITE, [player_icon_x, player_icon_y, player_icon_size, player_icon_size], 3)
    red_text = FONT_s.render("Red", True, WHITE)
    WINDOW.blit(red_text, [player_icon_size + player_icon_x*2, player_icon_y])
    player_list = open_file('red.txt')

    red_net_worth_int = player_list[1]
    red_net_worth = FONT_s.render(f"Net Worth: {red_net_worth_int}", True, WHITE)
    WINDOW.blit(red_net_worth, [player_icon_size + player_icon_x*2, player_icon_y + red_text.get_height()])
    
    red_properties_int = player_list[0]
    red_properties = FONT_s.render(f"Properties: {red_properties_int}", True, WHITE)
    WINDOW.blit(red_properties, [player_icon_size + player_icon_x*2, player_icon_y + red_text.get_height() + red_net_worth.get_height()])

    text_width = player_icon_size + player_icon_x*2 + red_net_worth.get_width()

    if  text_width > WINDOW.get_width() * BOARD_START_POS:
        smallsize = 15

    pygame.draw.rect(WINDOW, WHITE, [player_icon_x, player_icon_y*2 + player_icon_size, player_icon_size, player_icon_size], 3)
    green_text = FONT_s.render("Green", True, WHITE)
    WINDOW.blit(green_text, [player_icon_size + player_icon_x*2, player_icon_y*2 + player_icon_size ])
    player_list = open_file('green.txt')

    green_net_worth_int = player_list[1]
    green_net_worth = FONT_s.render(f"Net Worth: {green_net_worth_int}", True, WHITE)
    WINDOW.blit(green_net_worth, [player_icon_size + player_icon_x*2, player_icon_y*2 + player_icon_size + green_text.get_height()])
    
    green_properties_int = player_list[0]
    green_properties = FONT_s.render(f"Properties: {green_properties_int}", True, WHITE)
    WINDOW.blit(green_properties, [player_icon_size + player_icon_x*2, player_icon_y*2 + player_icon_size + green_text.get_height() + green_net_worth.get_height()])


    pygame.draw.rect(WINDOW, WHITE, [player_icon_x, player_icon_y*3 + player_icon_size * 2, player_icon_size, player_icon_size], 3)
    blue_text = FONT_s.render("Blue", True, WHITE)
    WINDOW.blit(blue_text, [player_icon_size + player_icon_x*2, player_icon_y*3 + player_icon_size * 2 ])
    player_list = open_file('blue.txt')

    blue_net_worth_int = player_list[1]
    blue_net_worth = FONT_s.render(f"Net Worth: {blue_net_worth_int}", True, WHITE)
    WINDOW.blit(blue_net_worth, [player_icon_size + player_icon_x*2, player_icon_y*3 + player_icon_size * 2  + blue_text.get_height()])

    blue_properties_int = player_list[0]
    blue_properties = FONT_s.render(f"Properties: {blue_properties_int}", True, WHITE)
    WINDOW.blit(blue_properties, [player_icon_size + player_icon_x*2, player_icon_y*3 + player_icon_size * 2  + blue_text.get_height() + blue_net_worth.get_height()])


    pygame.draw.rect(WINDOW, WHITE, [player_icon_x, player_icon_y*4 + player_icon_size * 3, player_icon_size, player_icon_size], 3)
    yellow_text = FONT_s.render("Yellow", True, WHITE)
    WINDOW.blit(yellow_text, [player_icon_size + player_icon_x*2, player_icon_y*4 + player_icon_size * 3 ])
    player_list = open_file('yellow.txt')

    yellow_net_worth_int = player_list[1]
    yellow_net_worth = FONT_s.render(f"Net Worth: {yellow_net_worth_int}", True, WHITE)
    WINDOW.blit(yellow_net_worth, [player_icon_size + player_icon_x*2, player_icon_y*4 + player_icon_size * 3   + yellow_text.get_height()])

    yellow_properties_int = player_list[0]
    yellow_properties = FONT_s.render(f"Properties: {yellow_properties_int}", True, WHITE)
    WINDOW.blit(yellow_properties, [player_icon_size + player_icon_x*2, player_icon_y*4 + player_icon_size * 3   + yellow_text.get_height() + yellow_net_worth.get_height()])


    #drawing the bank's box
    #<<<<<<<<<<<<<<<------------------------------------------>>>>>>>>>>>>>>>>>>>
    draw_rectangle(player_icon_x, player_icon_y * 5 + player_icon_size * 4, BOARD_START_POS*WINDOW.get_width() - 20, MID_RECT_WIDTH*8)
    bank_text = FONT_s.render("BANK", True, WHITE)
    WINDOW.blit(bank_text, [player_icon_x*2, player_icon_y * 6 - 10 + player_icon_size * 4])
    player_list = open_file('bank.txt')

    bank_net_worth_int = player_list[1]
    bank_net_worth = FONT_s.render(f"Net Worth: {bank_net_worth_int}", True, WHITE)
    WINDOW.blit(bank_net_worth, [player_icon_x*2, player_icon_y * 6 - 10 + player_icon_size * 4 + bank_text.get_height()])

    bank_properties_int = player_list[0]
    bank_properties = FONT_s.render(f"Properties: {bank_properties_int}", True, WHITE)
    WINDOW.blit(bank_properties, [player_icon_x*2, player_icon_y * 6 - 10 + player_icon_size * 4 + bank_text.get_height()*2])

    #Drawing the console
    #<<<<<<<<<<<<<<<------------------------------------------>>>>>>>>>>>>>>>>>>>
    # draw_rectangle(player_icon_x, MID_RECT_WIDTH*8 + 20, BOARD_START_POS*WINDOW.get_width() - 20, BOARD_SIZE)
    # console_text = FONT_s.render("CONSOLE", True, WHITE)
    # WINDOW.blit(console_text, [player_icon_x * 2, MID_RECT_WIDTH*8 + 30])

    

    # console_write(WINDOW, "Hi how are you", MID_RECT_WIDTH)

    