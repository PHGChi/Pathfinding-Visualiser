import pygame
from Helper.GlobalVariables import *
from Helper.TextHelper import DrawText, DrawTextCenter
from Helper.ButtonHelper import Button

def HelpSlides():
    # Dimensions
    helpWidth = 600
    helpHeight = 325
    # Create new window
    helpWin = pygame.display.set_mode((helpWidth, helpHeight))
    pygame.display.set_caption("Help")
    pygame.init()

    helpWin.fill(WHITE)

    # Define buttons
    btnPrevious = Button(0, 100, 80, 30, WHITE, BLACK, "Previous", "Normal")
    btnNext = Button(50, 100, 80, 30, WHITE, BLACK, "Next", "Normal")

    # First slide
    font = pygame.font.SysFont('sans-serif', 50)
    DrawTextCenter("Hi", font, helpWin, WIDTH // 2, HEIGHT // 2, BLACK)
    pygame.display.update()

    slide = 1
    run = True
    while run:
        for event in pygame.event.get():
            # If user wants to quit
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: # Left clicked
                pos = pygame.mouse.get_pos()

                # Check if "Previous" button is clicked
                if btnPrevious.rect.collidepoint(pos):
                    if slide <= 1:
                        slide == 1
                    else:
                        slide -= 1

                # Check if "Next" button is clicked
                if btnNext.rect.collidepoint(pos):
                    if slide >= 2:
                        slide == 2
                    else:
                        slide += 1

        # Draw current clide based on slide number
        if slide == 1:
            helpWin.fill(WHITE)
            DrawTextCenter("Hi", font, helpWin, helpWidth // 2, helpHeight // 2, BLACK)
        elif slide == 2:
            helpWin.fill(WHITE)
            DrawTextCenter("Bye", font, helpWin, helpWidth // 2, helpHeight // 2, BLACK)

        # Draw buttons
        btnPrevious.Draw(helpWin)
        btnNext.Draw(helpWin)

        pygame.display.update()
            



