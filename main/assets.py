import pygame, sys
pygame.init()

def get_font(choice, size):
    if choice == "menu":
        return pygame.font.Font("Assets/Font.ttf", size)
    elif choice == "help":
        return pygame.font.Font("Assets/Dhurjati.ttf", size)

music = pygame.mixer.music.load("Assets/Menu Music.mp3")
click_music = pygame.mixer.Sound("Assets/Click.mp3")
hover_sound = pygame.mixer.Sound("Assets/Hover.mp3")
WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
BG = pygame.image.load("Assets/Background(2).png")