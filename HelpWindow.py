import pygame
import pygame.image
import os.path
from Helper.GlobalVariables import *

def HelpSlides():
    # Dimensions
    helpWidth = 600
    helpHeight = 600

    # Create new window
    helpWin = pygame.display.set_mode((helpWidth, helpHeight))
    pygame.display.set_caption("Help")
    pygame.init()

    helpWin.fill(WHITE)

    # Define slides' content
    slides = [
        pygame.transform.scale(pygame.image.load(os.path.join('HelpGuideImages', '1.png')), (helpWidth, helpHeight)),
        pygame.transform.scale(pygame.image.load(os.path.join('HelpGuideImages', '2.png')), (helpWidth, helpHeight)),
        pygame.transform.scale(pygame.image.load(os.path.join('HelpGuideImages', '3.png')), (helpWidth, helpHeight)),
        pygame.transform.scale(pygame.image.load(os.path.join('HelpGuideImages', '4.png')), (helpWidth, helpHeight)),
        pygame.transform.scale(pygame.image.load(os.path.join('HelpGuideImages', '5.png')), (helpWidth, helpHeight)),
        pygame.transform.scale(pygame.image.load(os.path.join('HelpGuideImages', '6.png')), (helpWidth, helpHeight)),
        pygame.transform.scale(pygame.image.load(os.path.join('HelpGuideImages', '7.png')), (helpWidth, helpHeight))
    ]

    slide = 0
    run = True
    while run:
        for event in pygame.event.get():
            # If user wants to quit
            if event.type == pygame.QUIT:
                run = False

            # Change button colour when hovered over
            btnExit.Check()
            btnPrevious.Check()
            btnNext.Check()

            if event.type == pygame.MOUSEBUTTONDOWN: # Left clicked
                pos = pygame.mouse.get_pos()
                
                # Exit help guide when "Exit" button is clicked
                if btnExit.Check():
                    run = False

                # Move to previous slide when "Previous" button is clicked
                if btnPrevious.Check():
                    if slide <= 0:
                        slide == 0
                    else:
                        slide -= 1

                # Move to next slide when "Next" button is clicked
                if btnNext.Check():
                    if slide >= 6:
                        slide == 6
                    else:
                        slide += 1

        # Draw the slides
        helpWin.fill(WHITE)
        slideContent = slides[slide]
        helpWin.blit(slideContent, (0, 0))

        # Draw buttons
        btnExit.Draw(helpWin)
        if slide > 0: 
            btnPrevious.Draw(helpWin)
        if slide < 6:
            btnNext.Draw(helpWin)

        pygame.display.update()
            



