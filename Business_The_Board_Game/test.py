import sys
import pygame
import os
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()
 
os.environ['SDL_VIDEO_CENTERED'] = '1'
display_info = pygame.display.Info()

# WIDTH, HEIGHT = display_info.current_w, display_info.current_h
WIDTH, HEIGHT = 900, 700

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT - 50), pygame.RESIZABLE)
pygame.display.set_caption("Business - The Board Game")

FPS = 60

FONT_s = pygame.font.SysFont('comicsans', 25)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

start_pos_x, start_pos_y = 10, 10
box_height = 50
box_width = 200
offset = 10

radius = 15

t1_x, t1_y = start_pos_x+box_width - offset*4, start_pos_y + box_height/2

def draw_rectangle(start_pos_x, start_pos_y, end_pos_x, end_pos_y):
    widht = end_pos_x - start_pos_x
    hight = end_pos_y - start_pos_y
    pygame.draw.rect(WINDOW, WHITE, [start_pos_x, start_pos_y, widht, hight], 3)


def draw(temp_x, temp_y):

    pygame.draw.rect(WINDOW, WHITE, [start_pos_x, start_pos_y, box_width, box_height], 3)
    pygame.draw.rect(WINDOW, WHITE, [start_pos_x, start_pos_y + box_height + offset, box_width, box_height], 3)
    pygame.draw.rect(WINDOW, WHITE, [start_pos_x, start_pos_y + box_height*2 + offset*2, box_width, box_height], 3)
    pygame.draw.rect(WINDOW, WHITE, [start_pos_x, start_pos_y + box_height*3 + offset*3, box_width, box_height], 3)
    pygame.draw.rect(WINDOW, WHITE, [start_pos_x, start_pos_y + box_height*4 + offset*4, box_width, box_height], 3)
    pygame.draw.rect(WINDOW, WHITE, [start_pos_x, start_pos_y + box_height*5 + offset*5, box_width, box_height], 3)

    #Generate text
    pygame.draw.rect(WINDOW, WHITE, [start_pos_x + box_width + offset, start_pos_y,  box_width, box_height], 3)
    generate_text = FONT_s.render("Click to move", True, WHITE)
    WINDOW.blit(generate_text, [start_pos_x + box_width + offset*3, start_pos_y + offset/2])

    #Draw token
    pygame.draw.circle(WINDOW, WHITE, [temp_x, temp_y], radius)

def move(random_numer, temp_x, temp_y):
    # for i in range(0, random_numer):
    temp_y += box_height + start_pos_y

    t1_x = temp_x
    t1_y = temp_y

    # draw_circle(temp_x, temp_y)
    return temp_x, temp_y

def draw_circle(temp_x, temp_y):
    pygame.draw.circle(WINDOW, WHITE, [temp_x, temp_y], radius)


def if_clicked(click_x, click_y, random_numer):

    if (click_x >= start_pos_x and click_x <= start_pos_x+box_width) and (click_y >= start_pos_y and click_y <= start_pos_y+box_height):
        print("CLick in the square")
    elif (click_x >= start_pos_x and click_x <= start_pos_x+box_width) and (click_y >= start_pos_y+box_height+offset and click_y <= start_pos_y+box_height+offset + box_height):
        print("CLick in the square")
    elif (click_x >= start_pos_x and click_x <= start_pos_x+box_width) and (click_y >= start_pos_y+box_height*2+offset*2 and click_y <= start_pos_y+box_height*2+offset*2 + box_height):
        print("CLick in the square")
    elif (click_x >= start_pos_x and click_x <= start_pos_x+box_width) and (click_y >= start_pos_y+box_height*3+offset*3 and click_y <= start_pos_y+box_height*3+offset*3 + box_height):
        print("CLick in the square")
    elif (click_x >= start_pos_x and click_x <= start_pos_x+box_width) and (click_y >= start_pos_y+box_height*4+offset*4 and click_y <= start_pos_y+box_height*4+offset*4 + box_height):
        print("CLick in the square")
    elif (click_x >= start_pos_x and click_x <= start_pos_x+box_width) and (click_y >= start_pos_y+box_height*5+offset*5 and click_y <= start_pos_y+box_height*5+offset*5 + box_height):
        print("CLick in the square")

    if (click_x >= start_pos_x + box_width + offset and click_x <= start_pos_x + box_width + offset + box_width) and (click_y >= start_pos_y and click_y <= start_pos_y+box_height):
        move(random_numer, t1_x, t1_y)
    

clock = pygame.time.Clock()

def main():
    random_number = 0
    n1, n2 = t1_x, t1_y

    running = True
    while running:  
        click_x = 0
        click_y = 0
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    random_number = random.randint(1, 6)
                    print(random_number)

            if event.type == pygame.MOUSEBUTTONDOWN:
            #    print(event)
               click_x = event.pos[0]
               click_y = event.pos[1]
            #    print(event.button)
            #    print(event.x, event.y)
            #    print(event.flipped)
            #    print(event.which)
        
            
        # m_pos = pygame.mouse.get_pos()
        # print(m_pos)

        if (click_x >= start_pos_x + box_width + offset and click_x <= start_pos_x + box_width + offset + box_width) and (click_y >= start_pos_y and click_y <= start_pos_y+box_height):
            n1, n2 = move(random_number, n1, n2)

        WINDOW.fill(BLACK)
        draw(n1, n2)
        if_clicked(click_x, click_y, random_number)

        pygame.display.update()
        
main()