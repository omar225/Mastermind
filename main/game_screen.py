import pygame
from pygame import Color

from game_settings import*
from game_assets  import*
from resourse_path import resource_path
from assets import get_font, click_music
from assets import music
from ui import Button
from spirtes import*



class Game:
    def __init__(self,screen):
        pygame.mixer.music.set_volume(0.3)
        self.screen = screen
        self.screen = pygame.display.set_mode(screen_size,pygame.FULLSCREEN)
        self.screen_background = pygame.image.load(SCREEN_BACKGROUND)
        self.board_background = pygame.image.load(BOARD_BACKGROUND)
        self.clock = pygame.time.Clock()
        self.back_button_clicked = False

        back_button_image = pygame.image.load(resource_path("Assets/Back-Button.png"))
        back_button_image = pygame.transform.scale(back_button_image, (100, 50))
        self.back_button = Button(
            image=back_button_image,
            pos=(130, 95),  # Top-left corner
            text_input="",
            font=get_font("menu", 20),  # Assuming `get_font` is implemented elsewhere
            base_color="White",
            hovering_color="#b68f40"
        )

    def new(self):
        self.board = Board()
        self.color = None
        self.back_button_clicked = False

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen with black
        self.screen.blit(self.screen_background,(0,0))
        scaled_board_background = pygame.transform.scale(self.board_background,(width,height))
        self.screen.blit(scaled_board_background, board_offset)
        self.board.draw(self.screen,BLACK,board_offset)

        #back button
        self.back_button.changeColor(pygame.mouse.get_pos())
        self.back_button.update(self.screen)

        pygame.display.flip()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    click_music.play()  # Assuming `click_music` is defined
                    self.back_button_clicked = True
                    self.playing = False  # Exit game to go back to the main menu
                    return

                mx, my = event.pos
                self.color = self.board.select_color(mx,my,self.color)
                if self.color is not None:
                    self.board.place_pin(mx,my,self.color)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if self.board.check_row():
                        clues_color_list = self.board.check_clues()
                        self.board.set_clues(clues_color_list)
                        if self.check_win(clues_color_list):
                            print("YOU WON!")
                            self.board.reveal_code()
                            self.end_screen(True)

                        elif not self.board.next_round():
                            print("GAME OVER!!")
                            self.board.reveal_code()
                            self.end_screen(False)



    def check_win(self,color_list):
        return len(color_list) == 4 and all(color == BLACK for color in color_list)

    def end_screen(self, win):
        """
        Displays an end screen with a win/lose message, sprite, and sound.

        :param win: True if the player won, False otherwise.
        """
        # Load appropriate sprite and sound
        if win:
            message = "YOU WON!"
            sprite = pygame.image.load(resource_path("Assets/HappyFace.png"))
            sound = pygame.mixer.Sound(resource_path("Assets/WinSound.mp3"))
        else:
            message = "YOU LOSE!"
            sprite = pygame.image.load(resource_path("Assets/SadFace.png"))
            sound = pygame.mixer.Sound(resource_path("Assets/LoseSound.mp3"))

        # Scale sprite to fit nicely on the screen
        sprite = pygame.transform.scale(sprite, (200, 200))

        # Play the sound
        sound.play()

        # Draw static background and board
        self.draw()

        # Display sprite
        self.screen.blit(sprite, (width // 2 - 0, height // 2 - 150))  # Display sprite

        # Adjust text size and position
        smaller_font = get_font("menu", 50)  # Use a smaller font size
        text = smaller_font.render(message, True, "White")

        # Move text to the right side of the screen
        text_rect = text.get_rect(center=(width - 50, height // 2 + 100))  # Adjusted for right positioning
        self.screen.blit(text, text_rect)  # Display message

        pygame.display.flip()  # Update the screen

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key in {pygame.K_SPACE, pygame.K_RETURN}:
                        self.new()  # Create a new game
                        return  # Exit the end screen
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.back_button.checkForInput(pygame.mouse.get_pos()):
                        click_music.play()
                        self.back_button_clicked = True
                        self.playing = False
                        return


