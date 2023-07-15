import pygame
from Helper.TextHelper import DrawText, DrawTextCenter

class Button(object):
    global screenWidth, screenHeight, screen
    def __init__(self, x, y, width, height, textColour, backgroundColour, text, border=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textColour = textColour
        self.backgroundColour = backgroundColour
        self.border = border
        self.angle = 0

    #Check whether the mouse cursor is currently over the button
    def Check(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    #Draw the buttons
    def Draw(self, WIN):
        borderColour = "#9B9B9B" #Fix this
        pygame.draw.rect(WIN, self.backgroundColour, (self.rect), 0)

        if self.border:
            pygame.draw.rect(WIN, borderColour, (self.rect), 1) #Draw border
        
        if self.text == "PATHFINDING": #Set font for the heading
            font = pygame.font.SysFont('sans-serif', 24)
        else:
            font = pygame.font.SysFont('sans-serif', 20)
        DrawTextCenter(self.text, font, WIN, self.x+self.width/2, self.y+self.height/2, self.textColour)