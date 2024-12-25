import random

import pygame
from pygame.draw_py import draw_line
from game_assets import*
from game_settings import*


class Pin:
    def __init__(self,x,y,color=None, revealed = True):
        self.x = x
        self.y = y
        self.color = color
        self.revealed = revealed

    def draw(self,screen):
        center = (self.x + (tile_size/2), self.y + (tile_size/2))

        if self.color is not None and self.revealed:
            pygame.draw.circle(screen, tuple(x * 0.3 for x in self.color),tuple(x+3 for x in center),15)
            pygame.draw.circle(screen,self.color,center,15)

        elif not self.revealed:
            pygame.draw.circle(screen,LIGHTGREY,center,15)
            pygame.draw.circle(screen, BLACK, center, 15,3)
        else:
            pygame.draw.circle(screen,DARKBROWN,center,10)

class CluePin(Pin):
    def draw(self,screen):
        center = (self.x + (tile_size / 2.5), self.y + (tile_size / 2.5))
        if self.color is not None:
            pygame.draw.circle(screen,self.color,center,6)
        else:
            pygame.draw.circle(screen, DARKBROWN, center, 5)









class Board:
    def __init__(self):
        self.tries = 10
        self.board_background = pygame.image.load(BOARD_BACKGROUND)
        self.pins_surface = pygame.Surface((4*tile_size,11*tile_size))
        self.pins_surface.fill(BGCOLOUR)

        self.clue_surface = pygame.Surface((tile_size,11*tile_size))
        self.clue_surface.fill(BGCOLOUR)

        self.color_selection_surface = pygame.Surface((4*tile_size,2*tile_size))
        self.color_selection_surface.fill(LIGHTGREY)

        self.color_selection = []
        self.board_pins = []
        self.board_clues = []

        self.create_selection_pins()
        self.create_pins()
        self.create_clues()
        self.create_code()

    def create_clues(self):
        for i in range (1,11):
            temp_row = []
            for row in range(2):
                for col in range(2):
                    temp_row.append(CluePin(col * (tile_size//4),(row * (tile_size//4)) + i * tile_size))
            self.board_clues.append(temp_row)

    def create_pins(self):
        for row in range(11):
            temp_row = []
            for col in range(4):
                temp_row.append(Pin(col*tile_size,row*tile_size))
            self.board_pins.append(temp_row)



    def create_selection_pins(self):
        color_index = 0
        for y in range(2):
            for x in range(4):
                if color_index < amount_colors:
                    self.color_selection.append(Pin(x*tile_size, y*tile_size,COLORS[color_index]))
                    color_index += 1
                else:
                    break


    def draw(self,screen,color,offset=(0,0)):

        # draw pin selection
        for pin in self.color_selection:
            pin.draw(self.color_selection_surface)

        # draw pins
        for row in self.board_pins:
            for pin in row:
                pin.draw(self.pins_surface)

        # draw clue pins
        for row in self.board_clues:
            for pin in row:
                pin.draw(self.clue_surface)

        screen.blit(self.pins_surface,offset)
        screen.blit(self.clue_surface, (offset[0]+(4*tile_size),offset[1]))
        screen.blit(self.color_selection_surface, (offset[0], offset[1]+(11*tile_size)))

        # draw row indicator
        if self.tries > 0:

            pygame.draw.rect(screen,GREEN,(board_offset[0],(tile_size*self.tries)+board_offset[1],4*tile_size,tile_size),2)

        for x in range(0,width,tile_size):
            for y in range(0,height,tile_size):
                pygame.draw.line(screen,color, (offset[0] + x,offset[1]),(offset[0] + x,height+offset[1]))
                pygame.draw.line(screen, color, (offset[0], offset[1] + y), (width+offset[0], offset[1] + y))


    def select_color(self,mx,my,previous_color):

        for pin in self.color_selection:
            if pin.x < mx - board_offset[0] < pin.x + tile_size and pin.y < my - (board_offset[1]+11*tile_size) < pin.y + tile_size:
                return  pin.color

        return previous_color

    def place_pin(self,mx,my,color):
        for pin in self.board_pins[self.tries]:
            if pin.x < mx - board_offset[0] < pin.x + tile_size and pin.y < my - board_offset[1] < pin.y + tile_size:
                pin.color = color
                break


    def check_row(self):
        for pin in self.board_pins[self.tries]:
            if pin.color is None:
                return False

        return True

    def check_clues(self):
        color_list = []
        for i, code_pin in enumerate(self.board_pins[0]):
            color = None
            for j, user_pin in enumerate(self.board_pins[self.tries]):
                if user_pin.color == code_pin.color:
                    color = WHITE
                    if i == j:
                        color = BLACK
                        break

            if color is not None:
                color_list.append(color)

        color_list.sort()
        return color_list

    def set_clues(self,color_list):
        for color, pin in zip(color_list, self.board_clues[self.tries-1]):
            pin.color = color

    def create_code(self):
        random_code = random.sample(COLORS,4)
        for i, pin in enumerate(self.board_pins[0]):
            pin.color = random_code[i]
            pin.revealed = False

    def next_round(self):
        self.tries -= 1
        return self.tries > 0


    def reveal_code(self):
        for pin in self.board_pins[0]:
            pin.revealed = True







