import pygame

class streak():
    def __init__(self, screen, position):
        self.currentStreak = 0
        self.addStreak = False
        self.screen = screen
        self.position = position
        self.font = pygame.font.SysFont('Arial', 16, bold=True)

    def get(self):
        return self.currentStreak

    def increase(self):
        self.currentStreak += 1
    
    def draw(self):
        streakMessage = "Streak:" + str(self.currentStreak)
        displayStreak = self.font.render(streakMessage, True, (0, 0, 0))
        self.screen.blit(displayStreak, self.position)
