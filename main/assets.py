import pygame, sys
pygame.init()

def get_font(choice, size):
    if choice == "menu":
        return pygame.font.Font("main\Assets\Font.ttf", size)
    elif choice == "help":
        return pygame.font.Font("main\Assets\Dhurjati.ttf", size)

music = pygame.mixer.music.load("main\Assets\Menu Music.mp3")
click_music = pygame.mixer.Sound("main\Assets\Click.mp3")
WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.image.load("main\Assets\Background(2).png")