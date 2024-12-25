import pygame, sys

from resourse_path import resource_path
from ui import Button
from assets import WIDTH, HEIGHT, BG, SCREEN, click_music,get_font

pygame.display.set_caption("Help Menu")

def help():
    while True:
        HELP_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))
        
        instructions = ["",
            "INSTRUCTIONS",
            "The computer will select a secret code consisting of 4 colors.",
            "Your task is to guess the code by placing colored pegs in the empty slots.",
            "After each guess, the computer will provide feedback in the form of black and white pegs.",
            "A black peg means a correct color in the correct position.",
            "A white peg means a correct color in the wrong position.",
            "Use this feedback to deduce the correct code within 10 turns.",
            "Click on the colored pegs to select them, then click on the slots to place them.",
            "Click the 'Enter' button to submit your guess and receive feedback.",
        ]
        
        for line in instructions:
            height_offset = instructions.index(line) * 90
            HELP_TEXT = get_font("help", 45).render(line, True, "White")
            HELP_RECT = HELP_TEXT.get_rect(center=(800, height_offset))
            SCREEN.blit(HELP_TEXT, HELP_RECT)

        back_button_image = pygame.image.load(resource_path("Assets/Back-Button.png"))
        back_button_image = pygame.transform.scale(back_button_image, (100, 50))
        HELP_BACK = Button(image=back_button_image, pos=(130, 95), 
                            text_input="", font=get_font("menu", 20), base_color="White", hovering_color="#b68f40")

        HELP_BACK.changeColor(HELP_MOUSE_POS)
        HELP_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HELP_BACK.checkForInput(HELP_MOUSE_POS):
                    click_music.play()
                    return 1

        pygame.display.update()