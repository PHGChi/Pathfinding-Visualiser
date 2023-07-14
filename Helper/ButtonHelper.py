import pygame
from Helper.TextHelper import DrawText, DrawTextCenter

class Button(object):
    global screenWidth, screenHeight, screen
    def __init__(self, x, y, width, height, textColour, backgroundColour, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textColour = textColour
        self.backgroundColour = backgroundColour
        self.angle = 0

    #Check whether the mouse cursor is currently over the button
    def Check(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    #Draw the buttons
    def Draw(self, WIN):
        pygame.draw.rect(WIN, self.backgroundColour, (self.rect), 0)
        DrawTextCenter(self.text, pygame.font.SysFont('Calibri', 18), WIN, self.x+self.width/2, self.y+self.height/2, self.textColour)
        #Draw a border around the button
        pygame.draw.rect(WIN, self.textColour, self.rect, 3)