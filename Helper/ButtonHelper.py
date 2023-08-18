import pygame
from Helper.TextHelper import DrawTextCenter

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
        self.borderColour = "#C6C6C6"
        self.state = "normal"

    # Check the state of the button
    def Check(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]: # Mouse left clicked
                self.state = "clicked"
            else:
                self.state = "hovered"
            return True
        else:
            self.state = "normal"
            return False
    
    # Updating button's text
    def UpdateText(self, newText):
        self.text = newText
    
    # Draw the buttons
    def Draw(self, WIN):
        # Update background colour based on button's state
        if self.type == "Normal":
            if self.state == "clicked":
                self.backgroundColour = "#9B9B9B"
            elif self.state == "hovered":
                self.backgroundColour = "#00A67E"
            else: # Normal
                self.backgroundColour = "#4C5270"

        # Update background colour based on visualised button's state
        if self.type == "Visualise":
            if self.state == "clicked":
                self.backgroundColour = "#9B9B9B"
            elif self.state == "hovered":
                self.backgroundColour = "#00A67E"
            else: # Normal
                self.backgroundColour = "#69B27A"

        # Update help button colour based on state
        if self.type == "Help":
            if self.state == "clicked":
                self.textColour = "#C6C6C6"
                self.borderColour = "#C6C6C6"
            elif self.state == "hovered":
                self.textColour = "#9B9B9B"
                self.borderColour = "#9B9B9B"
            else: # Normal
                self.textColour = "#4C5270"
                self.borderColour = "#4C5270"

        pygame.draw.rect(WIN, self.backgroundColour, (self.rect), 0)

        # Draw border for legend symbols
        if self.border:
            pygame.draw.rect(WIN, self.borderColour, (self.rect), 1) 
        
        if self.type == "Title" or self.type == "No Path": # Set font for the title
            font = pygame.font.SysFont('sans-serif', 24)
        elif self.type == "Heading": #Set font for the headings
            font = pygame.font.SysFont('sans-serif', 22)
        else:
            font = pygame.font.SysFont('sans-serif', 20)
        DrawTextCenter(self.text, font, WIN, self.x+self.width/2, self.y+self.height/2, self.textColour)