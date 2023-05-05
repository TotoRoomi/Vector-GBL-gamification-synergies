import pygame
import Gameloop
import checkbox
import Buttons


font = pygame.font.SysFont('Arial', 20, bold=False) 
font2 = pygame.font.SysFont('Arial', 20, bold=False) 

xMark = font.render("X", True, "white")
informationTxt = font2.render("Choose game elements:", True, "black")
scoreTxt = font.render("Add score", True, "black")
streakTxt = font.render("Add streak", True, "black")
leaderboardTxt = font.render("Add leaderboard", True, "black")
differentGoalsTxt = font.render("Add different goals", True, "black") 
winningConditionTxt = font.render("Add winning condition", True, "black")
loosingConditionTxt = font.render("Add losing condition", True, "black")



def main():
    hasScore = False
    hasStreak = False
    hasLeaderboard = False
    hasDifferentGoals = False
    hasWinningCondition = False
    hasLoosingCondition = False
    # Simple pygame program
 
    # Import and initialize the pygame library
    pygame.init()
 
    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])
    
    # Run until the user asks to quit
    running = True

    start            =  Buttons.Button(screen, 200, 120, 100,60,'START')
    score            =  Buttons.Button(screen, 40, 240,20,20,'')
    streak           =  Buttons.Button(screen, 40, 280,20,20,'')
    leaderboard      =  Buttons.Button(screen, 40, 320,20,20,'')
    differentGoals   =  Buttons.Button(screen, 40, 360,20,20,'')
    winningCondition =  Buttons.Button(screen, 40, 400,20,20,'')
    loosingCondition =  Buttons.Button(screen, 40, 440,20,20,'')

    checkButtons = [start,score,streak,leaderboard, differentGoals,winningCondition,loosingCondition]

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
        screen.blit(leaderboardTxt, pygame.Vector2([80,239+80]))
        screen.blit(differentGoalsTxt, pygame.Vector2([80,239+120]))
        screen.blit(winningConditionTxt, pygame.Vector2([80,239+160]))
        screen.blit(loosingConditionTxt, pygame.Vector2([80,239+200]))

        # Draw buttons
        for button in checkButtons:
            button.process()
        
        # CLICK BUTTONS 
        if(checkButtons[0].buttonActive): # Start
            try:
                game = Gameloop.gameloop(screen, hasScore, hasStreak, hasLeaderboard, hasDifferentGoals, hasWinningCondition, hasLoosingCondition)
                game.start()
                screen = pygame.display.set_mode([500, 500])
                checkButtons[0].buttonActive = False # annars spammar den pga man "klickar" 60 ggr / sek
            except AttributeError:
                print('start doesnt work')
        if(checkButtons[1].buttonActive): # Score
            try:
                screen.blit(xMark, pygame.Vector2([43,239]))
                hasScore = True
            except AttributeError:
                print('start doesnt work')
        else: 
            hasScore = False
        if(checkButtons[2].buttonActive): # Streak
            try:
                hasStreak = True
                screen.blit(xMark, pygame.Vector2([43,279]))
            except AttributeError:
                print('start doesnt work')
        else:
            hasStreak = False
        if(checkButtons[3].buttonActive): # Leaderboard
            try:
                screen.blit(xMark, pygame.Vector2([43,319]))
                hasLeaderboard = True
            except AttributeError:
                print('start doesnt work')
        else:
            hasLeaderboard = False
        if(checkButtons[4].buttonActive): # differentGoals
            try:
                screen.blit(xMark, pygame.Vector2([40+3,360-1]))
                hasDifferentGoals = True
            except AttributeError:
                print('start doesnt work')
        else:
            hasDifferentGoals = False
        if(checkButtons[5].buttonActive): # winningCondition
            try:
                screen.blit(xMark, pygame.Vector2([40+3,400-1]))
                hasWinningCondition = True
            except AttributeError:
                print('start doesnt work')
        else: 
            hasWinningCondition = False
        if(checkButtons[6].buttonActive): # Loosing Condition
            try:
                screen.blit(xMark, pygame.Vector2([40+3,440-1]))
                hasLoosingCondition = True
            except AttributeError:
                print('start doesnt work')
        else:
            hasLoosingCondition = False

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    main()
