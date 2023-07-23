#Draw text centered at a specific position on the screen
def DrawTextCenter(text, font, screen, x, y, colour):
    textObj = font.render(text, True, colour)
    textRect = textObj.get_rect(center=((int)(x), (int)(y)))
    screen.blit(textObj, textRect)

#Draw text at a specific position on a surface
def DrawText(text, font, surface, x, y, colour):
    textObj = font.render(text, 1, colour)
    textRect = textObj.get_rect()
    textRect.topleft = (x,y)
    surface.blit(textObj, textRect)