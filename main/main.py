import pygame


from main_menu import main_menu,resource_path

pygame.init()

icon = pygame.image.load(resource_path("Assets/icon.png")) # Replace with the path to your icon
pygame.display.set_icon(icon)

main_menu()