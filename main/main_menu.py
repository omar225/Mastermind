import os
import sys

from resourse_path import resource_path
from game_screen import Game
import pygame, sys
from ui import Button
from assets import WIDTH, HEIGHT, BG, SCREEN, music, click_music, get_font,hover_sound
from help_screen import help

pygame.init()

pygame.display.set_caption("MasterMind")
pygame.mixer.music.play(-1)

def play():
    game = Game(SCREEN)
    while True:
        game.new()
        game.run()
        main_menu()
def help_import():
    if help() == 1:
        main_menu()

def fade_out(screen, color=(0, 0, 0), duration=500):
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill(color)
    for alpha in range(0, 255, 5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(duration // 51)



def main_menu():
    pygame.mixer.music.set_volume(1)
    hover_play = hover_help = hover_quit = False
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font("menu", 100).render("MASTERMIND", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(800, 125))

        PLAY_BUTTON = Button(image=pygame.image.load(resource_path("Assets/Play Rect(1).png")), pos=(800, 300),
                            text_input="PLAY", font=get_font("menu", 75), base_color="White", hovering_color="#b68f40")
        HELP_BUTTON = Button(image=pygame.image.load(resource_path("Assets/Help Rect(1).png")), pos=(800, 500),
                            text_input="HELP", font=get_font("menu", 75), base_color="White", hovering_color="#b68f40")
        QUIT_BUTTON = Button(image=pygame.image.load(resource_path("Assets/Quit Rect.png")), pos=(800, 700),
                            text_input="QUIT", font=get_font("menu", 75), base_color="White", hovering_color="#b68f40")

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
                    fade_out(SCREEN)
                    play()
                if HELP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_music.play()
                    help_import()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()

        pygame.display.update()