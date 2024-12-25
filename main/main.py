import pygame
from main_menu import main_menu

pygame.init()

icon = pygame.image.load("Assets/icon.png")  # Replace with the path to your icon
pygame.display.set_icon(icon)

main_menu()