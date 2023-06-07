import pygame

class score():
    def __init__(self, screen, position):
        self.currentScore = 0
        self.addScore = False
        self.screen = screen
        self.position = position 
        self.font = pygame.font.SysFont('Arial', 16, bold=True)

    def get(self):
        return self.currentScore

    def increase(self, multplier):
        self.currentScore += 1*multplier

    def manualIncrease(self, value):
        self.currentScore += value 
    
    def reset(self):
        self.currentScore = 0
    
    def draw(self):
        scoreMessage = "Score:" + str(self.currentScore)
        displayScore = self.font.render(scoreMessage, True, (0, 0, 0))
        self.screen.blit(displayScore, self.position)

