# Imports
import sys
import pygame

# Configuration
pygame.init()
'''

fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
'''

font = pygame.font.SysFont('Arial', 12)

objects = []

class Button():
    def __init__(self,screen, x, y, width, height, buttonText='Button', onePress=False):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onePress = onePress

        self.fillColors = {
            'normal': '#000000',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, "white")

        self.alreadyPressed = False
        self.buttonActive = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                
                if self.onePress:
                    self.buttonActive=True
                    #self.onclickFunction()

                elif not self.alreadyPressed:
                    #self.onclickFunction()
                    
                    if not self.buttonActive:
                        self.buttonActive=True
                        #self.onclickFunction()

                    elif self.buttonActive:
                        #self.onclickFunction()
                        self.buttonActive = False
                    self.alreadyPressed = True

                

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)
