import pygame
from Helper.TextHelper import DrawText, DrawTextCenter

class Button(object):
    global screenWidth, screenHeight, screen
    def __init__(self, x, y, width, height, textColour, backgroundColour, text, type, border=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textColour = textColour
        self.backgroundColour = backgroundColour
        self.type = type
        self.border = border
        if self.type == "Help":
            self.borderColour = "#4C5270"
        else:
            self.borderColour = "#9B9B9B"

    # Check whether the mouse cursor is currently over the button
    def Check(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    # Updating button's text
    def UpdateText(self, newText):
        self.text = newText
    
    # Draw the buttons
    def Draw(self, WIN):
        pygame.draw.rect(WIN, self.backgroundColour, (self.rect), 0)

        # Draw border for legend symbols
        if self.border:
            pygame.draw.rect(WIN, self.borderColour, (self.rect), 1) 
        
        if self.type == "Title": # Set font for the title
            font = pygame.font.SysFont('sans-serif', 24)
        elif self.type == "Heading": #Set font for the headings
            font = pygame.font.SysFont('sans-serif', 22)
        else:
            font = pygame.font.SysFont('sans-serif', 20)
        DrawTextCenter(self.text, font, WIN, self.x+self.width/2, self.y+self.height/2, self.textColour)