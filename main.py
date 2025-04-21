import pygame
from space_inv import run_space_invaders

images = "images/"

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Arcade")

font = pygame.font.Font(f"{images}Pixelify Sans.ttf", 36)
small_font = pygame.font.Font(f"{images}Pixelify Sans.ttf", 24)

WHITE = (255,255,255)
GRAY = (100,100,100)
BLACK = (0,0,0)

MAIN_MENU = 0
SPACE_INVADERS = 1
QUIT = 2

current_state = MAIN_MENU

def main_menu():
    screen.fill(BLACK)
    draw_text("Arcade",font,WHITE,250,100)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 300 <= mouse[0] <= 500 and 250 <= mouse[1] <= 300:
        pygame.draw.rect(screen, GRAY, (300,250,200,50))
        if click[0]:
            return SPACE_INVADERS
    else:
        pygame.draw.rect(screen, WHITE, (300,250,200,50))
    draw_text("Space Invaders", small_font, BLACK, 320, 260)

    if 300 <= mouse[0] <= 500 and 350 <= mouse[1] <= 400:
        pygame.draw.rect(screen, GRAY, (300,350,200,50))
        if click[0]:
            return QUIT
    else:
        pygame.draw.rect(screen, WHITE, (300,350,200,50))
    draw_text("Quit", small_font, BLACK, 370,360)

    pygame.display.update()
    return MAIN_MENU

def draw_text(text, font, color, x, y):
    render = font.render(text, True, color)
    screen.blit(render, (x,y))

while True:
    if current_state == MAIN_MENU:
        current_state = main_menu()
    elif current_state == SPACE_INVADERS:
        success = run_space_invaders(screen)
        current_state = MAIN_MENU if success else QUIT
    elif current_state == QUIT:
        break

pygame.quit()
