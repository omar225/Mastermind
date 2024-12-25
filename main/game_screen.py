import pygame
from pygame import Color

from game_settings import*
from game_assets  import*
from spirtes import*



class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(screen_size)
        self.screen_background = pygame.image.load(SCREEN_BACKGROUND)
        self.board_background = pygame.image.load(BOARD_BACKGROUND)
        self.clock = pygame.time.Clock()

    def new(self):
        self.board = Board()
        self.color = None

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def draw(self):
        self.screen.blit(self.screen_background,(0,0))
        scaled_board_background = pygame.transform.scale(self.board_background,(width,height))
        self.screen.blit(scaled_board_background, board_offset)
        self.board.draw(self.screen,BLACK,board_offset)
        pygame.display.flip()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                self.color = self.board.select_color(mx,my,self.color)
                if self.color is not None:
                    self.board.place_pin(mx,my,self.color)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or pygame.K_RETURN:
                    if self.board.check_row():
                        clues_color_list = self.board.check_clues()
                        self.board.set_clues(clues_color_list)
                        if self.check_win(clues_color_list):
                            print("YOU WON!")
                            self.board.reveal_code()
                            self.end_screen()

                        elif not self.board.next_round():
                            print("GAME OVER!!")
                            self.board.reveal_code()
                            self.end_screen()



    def check_win(self,color_list):
        return len(color_list) == 4 and all(color == BLACK for color in color_list)

    def end_screen(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    self.playing = False
                    return

            self.draw()


game = Game()

while True:
    game.new()
    game.run()
