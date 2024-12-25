import pygame

# game settings
rows = 13
columns = 5
amount_colors = 8
tile_size = 65

height= (rows * tile_size) + 1
width = (columns * tile_size) + 1

FPS = 60
title = "Mastermind"

screen_size = (1600, 900)
board_offset = (600,20) #(0,0)