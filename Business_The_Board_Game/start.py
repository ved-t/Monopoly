import pygame
import sys
import os


# Initialize Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
display_info = pygame.display.Info()

clock = pygame.time.Clock()
# Set up the window
WIDTH, HEIGHT = display_info.current_w, display_info.current_h
# WIDTH, HEIGHT = 900, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT - 50), pygame.RESIZABLE)
pygame.display.set_caption("Business - The Board Game")
FPS = 60
# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
Y_W = (242, 240, 223)
# Set up fonts
font = pygame.font.Font(None, 50)

# Set up buttons
start_button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 50, 250, 50)
rules_button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 50, 250, 50)
how_to_play_button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 150, 250, 50)
exit_button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 250, 250, 50)

def play_game():
    screen.fill(WHITE)
    game_label = font.render("Playing the Game!", True, BLACK)
    screen.blit(game_label, (WIDTH//2 - game_label.get_width() // 2, HEIGHT//2 - game_label.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(3000)  # Delay for 3 seconds

    player_buttons = [
        pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 150, 250, 50),  # 2 players button
        pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 50, 250, 50),   # 3 players button
        pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 50, 250, 50),   # 4 players button
    ]
    back_button_rect = pygame.Rect(20, 20, 100, 50)

    while True:
        screen.fill(WHITE)
       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, button in enumerate(player_buttons):
                    if button.collidepoint(mouse_pos):
                        player_count = i + 2  # Player count will be 2, 3, or 4
                        print("Selected Player Count:", player_count)
                if back_button_rect.collidepoint(mouse_pos):
                    return  # Return from the play_game() function to go back

        # Draw player count selection buttons
        for i, button in enumerate(player_buttons):
            pygame.draw.rect(screen, BLACK, button)
            player_label = font.render(f"{i+2} Players", True, WHITE)
            screen.blit(player_label, (button.x + 75, button.y + 10))

        # Draw back button
        pygame.draw.rect(screen, BLACK, back_button_rect)
        back_label = font.render("Back", True, WHITE)
        screen.blit(back_label, (back_button_rect.x + 10, back_button_rect.y + 10))

        pygame.display.flip()
        clock.tick(FPS)


def show_rules():
    back_button_rect = pygame.Rect(20, 20, 100, 50)

    while True:
        screen.fill(WHITE)
        rule_text = [
            "RULES:",
            "- Rule 1: ...",
            "- Rule 2: ...",
            "- Rule 3: ..."
        ]
        y_offset = 100

        for line in rule_text:
            rule_label = font.render(line, True, BLACK)
            screen.blit(rule_label, (WIDTH//2 - rule_label.get_width() // 2, y_offset))
            y_offset += 50

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button_rect.collidepoint(mouse_pos):
                    return  # Return from the show_rules() function to go back

        # Draw back button
        pygame.draw.rect(screen, BLACK, back_button_rect)
        back_label = font.render("Back", True, WHITE)
        screen.blit(back_label, (back_button_rect.x + 10, back_button_rect.y + 10))

        pygame.display.flip()
        clock.tick(FPS)


# Load the image
# image = pygame.image.load("bussiness_game.jpg")  # Replace "image.png" with your image file
# image = pygame.transform.scale(image, (WIDTH,HEIGHT))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_pos):
                play_game()
            elif rules_button_rect.collidepoint(mouse_pos):
                show_rules()
            elif exit_button_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    # Clear the screen
    screen.fill(RED)

    # Draw the image
    # screen.blit(image, (0, 0))  # Adjust the coordinates as needed

    # Draw the rectangle
    rectangle_rect = pygame.Rect(500,350, 600, 400)
    pygame.draw.rect(screen, Y_W, rectangle_rect)

    # Draw buttons
    pygame.draw.rect(screen, BLACK, start_button_rect)
    pygame.draw.rect(screen, BLACK, rules_button_rect)
    pygame.draw.rect(screen, BLACK, how_to_play_button_rect)
    pygame.draw.rect(screen, BLACK, exit_button_rect)

    # Draw button labels
    start_label = font.render("Start", True, WHITE)
    screen.blit(start_label, (start_button_rect.x + 75, start_button_rect.y + 10))
    rules_label = font.render("Rules", True, WHITE)
    screen.blit(rules_label, (rules_button_rect.x + 75, rules_button_rect.y + 10))
    how_to_play_label = font.render("How to play", True, WHITE)
    screen.blit(how_to_play_label, (how_to_play_button_rect.x + 25, how_to_play_button_rect.y + 15))
    exit_label = font.render("Exit", True, WHITE)
    screen.blit(exit_label, (exit_button_rect.x + 80, exit_button_rect.y + 10))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()