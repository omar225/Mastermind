import pygame, sys

from resourse_path import resource_path

pygame.init()

def get_font(choice, size):
    if choice == "menu":
        return pygame.font.Font(resource_path("Assets/Font.ttf"), size)
    elif choice == "help":
        return pygame.font.Font(resource_path("Assets/Dhurjati.ttf"), size)

music = pygame.mixer.music.load(resource_path("Assets/Menu Music.mp3"))
click_music = pygame.mixer.Sound(resource_path("Assets/Click.mp3"))
hover_sound = pygame.mixer.Sound(resource_path("Assets/Hover.mp3"))
WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
BG = pygame.image.load(resource_path("Assets/Background(2).png"))