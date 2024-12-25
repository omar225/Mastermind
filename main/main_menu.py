import pygame, sys
from game_assets import SCREEN_BACKGROUND
from ui import Button
from game_settings import screen_size

pygame.init()

SCREEN = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Menu")

BG = pygame.image.load(SCREEN_BACKGROUND)

music = pygame.mixer.music.load("Assets/Menu Music.mp3")
pygame.mixer.music.play(-1)
click_music = pygame.mixer.Sound("Assets/Click.mp3")
hover_sound = pygame.mixer.Sound("Assets/Hover.mp3")

def get_font(size):
    return pygame.font.Font("Assets/Font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(800, 360))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(800, 660), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="#b68f40")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    click_music.play()
                    main_menu()

        pygame.display.update()
    
def help():
    while True:
        HELP_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        HELP_TEXT = get_font(45).render("This is the HELP screen.", True, "White")
        HELP_RECT = HELP_TEXT.get_rect(center=(800, 360))
        SCREEN.blit(HELP_TEXT, HELP_RECT)

        HELP_BACK = Button(image=None, pos=(800, 660), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="#b68f40")

        HELP_BACK.changeColor(HELP_MOUSE_POS)
        HELP_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HELP_BACK.checkForInput(HELP_MOUSE_POS):
                    click_music.play()
                    main_menu()

        pygame.display.update()

def main_menu():

    hover_play = hover_help = hover_quit = False
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MASTERMIND", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(800, 125))

        PLAY_BUTTON = Button(image=pygame.image.load("Assets/Play Rect(1).png"), pos=(800, 300),
                            text_input="PLAY", font=get_font(75), base_color="White", hovering_color="#b68f40")
        HELP_BUTTON = Button(image=pygame.image.load("Assets/Help Rect(1).png"), pos=(800, 500),
                            text_input="HELP", font=get_font(75), base_color="White", hovering_color="#b68f40")
        QUIT_BUTTON = Button(image=pygame.image.load("Assets/Quit Rect.png"), pos=(800, 700),
                            text_input="QUIT", font=get_font(75), base_color="White", hovering_color="#b68f40")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        hover_sound.set_volume(0.15)

        for button in [PLAY_BUTTON, HELP_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if not hover_play:
                        hover_sound.play()
                        hover_play = True
                else:
                    hover_play = False
                if HELP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if not hover_help:
                        hover_sound.play()
                        hover_help= True
                else:
                    hover_help = False
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if not hover_quit:
                        hover_sound.play()
                        hover_quit = True
                else:
                    hover_quit = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_music.play()
                    play()
                if HELP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_music.play()
                    help()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()

        pygame.display.update()

main_menu()