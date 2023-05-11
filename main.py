import pygame
import Gameloop
import checkbox
import Leaderboard
import Buttons


font = pygame.font.SysFont('Arial', 20, bold=False) 
font2 = pygame.font.SysFont('Arial', 20, bold=False) 

xMark = font.render("X", True, "white")
informationTxt = font2.render("Choose game elements:", True, "black")
scoreTxt = font.render("Add score", True, "black")
streakTxt = font.render("Add streak", True, "black")
losingConditionTxt = font.render("Add losing condition", True, "black")
leaderboardTxt = font.render("Add leaderboard (needs score, streak, lose)", True, "black")
differentGoalsTxt = font.render("Add different goals", True, "black") 
# winningConditionTxt = font.render("Add winning condition", True, "black")



def main():
    hasScore = False
    hasStreak = False
    hasLosingCondition = False
    hasLeaderboard = False
    hasDifferentGoals = False
    # hasWinningCondition = False
    # Simple pygame program
 
    # Import and initialize the pygame library
    pygame.init()
 
    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])
    
    # Run until the user asks to quit
    running = True

    start            =  Buttons.Button(screen, 200, 55, 100,60,'START')
    leaderboardButton  =  Buttons.Button(screen, 200, 120, 100,60,'LEADERBOARD')
    score            =  Buttons.Button(screen, 40, 240,20,20,'')
    streak           =  Buttons.Button(screen, 40, 280,20,20,'')
    losingCondition  =  Buttons.Button(screen, 40, 320,20,20,'')
    leaderboardChk   =  Buttons.Button(screen, 40, 360,20,20,'')
    differentGoals   =  Buttons.Button(screen, 40, 400,20,20,'')

    while running:

    # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))
        
        # rendering text
        screen.blit(informationTxt, pygame.Vector2([80-40,239-40]))
        screen.blit(scoreTxt, pygame.Vector2([80,239]))
        screen.blit(streakTxt, pygame.Vector2([80,239+40]))
        screen.blit(losingConditionTxt, pygame.Vector2([80,239+80]))
        screen.blit(leaderboardTxt, pygame.Vector2([80,239+120]))
        screen.blit(differentGoalsTxt, pygame.Vector2([80,239+160]))
        # screen.blit(winningConditionTxt, pygame.Vector2([80,239+160]))

        # Draw buttons
        leaderboardButton.process() 
        start.process() 
        score.process() 
        streak.process() 
        losingCondition.process() 
        if(hasScore and hasStreak and hasLosingCondition):
            leaderboardChk.process() 
        else:
            pygame.draw.rect(screen, "gray", pygame.Rect(40, 360,20,20))
            hasLeaderboard = False
        differentGoals.process() 
        
        # CLICK BUTTONS 
        if(start.buttonActive): # Start
            try:
                game = Gameloop.gameloop(screen, hasScore, hasStreak, hasLeaderboard, hasDifferentGoals, hasLosingCondition)
                game.start()
                screen = pygame.display.set_mode([500, 500])
                start.buttonActive = False # annars spammar den pga man "klickar" 60 ggr / sek
            except AttributeError:
                print('start doesnt work')
        if(leaderboardButton.buttonActive):
            try:
                leaderboard = Leaderboard.leaderboard()  # Här kan man lägga in leaderboard writeTofile men det kommer inte sättas in förns två klick till.
                #leaderboard.window()
                leaderboard.saveScore(10,5)
                leaderboardButton.buttonActive = False # annars spammar den pga man "klickar" 60 ggr / sek
            except AttributeError:
                print('leaderboard menu button doesnt work')
        if(score.buttonActive): # Score
            try:
                screen.blit(xMark, pygame.Vector2([43,239]))
                hasScore = True
            except AttributeError:
                print('start doesnt work')
        else: 
            hasScore = False
        if(streak.buttonActive): # Streak
            try:
                hasStreak = True
                screen.blit(xMark, pygame.Vector2([43,279]))
            except AttributeError:
                print('start doesnt work')
        else:
            hasStreak = False
        if(losingCondition.buttonActive): # Losing condition
            try:
                screen.blit(xMark, pygame.Vector2([43,319]))
                hasLosingCondition = True
            except AttributeError:
                print('start doesnt work')
        else:
            hasLosingCondition = False
        if(leaderboardChk.buttonActive): # Leaderboard
            try:
                screen.blit(xMark, pygame.Vector2([40+3,360-1]))
                hasLeaderboard = True
            except AttributeError:
                print('start doesnt work')
        else:
            hasLeaderboard = False
        if(differentGoals.buttonActive): # Different Goals
            try:
                screen.blit(xMark, pygame.Vector2([40+3,400-1]))
                hasDifferentGoals = True
            except AttributeError:
                print('start doesnt work')
        else:
            hasDifferentGoals = False

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    main()
