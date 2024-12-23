import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)

# Fonts
FONT = pygame.font.Font("Font.ttf", 36)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mastermind Help Screen")

# Load background image
BG = pygame.image.load("Background(3).png")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))  # Scale the image to fit the screen dimensions

# Helper function to render text
def render_text(text, font, color, center):
    rendered_text = font.render(text, True, color)
    rect = rendered_text.get_rect(center=center)
    return rendered_text, rect

# Help screen function
def help_screen():
    while True:
        # Blit the background image
        screen.blit(BG, (0, 0))

        # Title
        title_text, title_rect = render_text("Help - Mastermind", FONT, WHITE, (WIDTH // 2, 50))
        screen.blit(title_text, title_rect)

        # Instructions
        instructions = [
            "Mastermind Instructions:",
            "1. The goal is to guess the hidden sequence of 4 colors.",
            "2. Each color can be Red, Green, Yellow, Blue, White, or Black.",
            "3. Use the keys 1-6 to select colors:",
            "   - 1 = Red, 2 = Green, 3 = Yellow, 4 = Blue, 5 = White, 6 = Black.",
            "4. Press Backspace to undo the last peg.",
            "5. Press Enter to submit your guess.",
            "6. Feedback:",
            "   - Black peg = Correct color in the correct position.",
            "   - White peg = Correct color in the wrong position.",
            "7. You have 10 attempts to guess the correct sequence.",
            "8. Press Esc to return to the main menu.",
        ]

        # Render instructions
        y_offset = 120
        for line in instructions:
            instruction_text, instruction_rect = render_text(line, pygame.font.Font("Font.ttf", 24), WHITE, (WIDTH // 2, y_offset))
            screen.blit(instruction_text, instruction_rect)
            y_offset += 30

        # Back button
        back_text, back_rect = render_text("Press Esc to go back", FONT, BLUE, (WIDTH // 2, HEIGHT - 50))
        screen.blit(back_text, back_rect)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Exit the help screen

# Run the help screen directly
if __name__ == "__main__":
    help_screen()


