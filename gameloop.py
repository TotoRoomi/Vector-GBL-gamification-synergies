
import pygame
import random
import Arrow
import Buttons
 
class gameloop():
    def __init__(self,screen,hasScore, hasStreak,hasLeaderboard, hasDifferentGoals,hasWinningCondition,hasLoosingCondition):
        
        self.screen                 = screen
        self.hasScore               = hasScore
        self.hasStreak              = hasStreak
        self.hasLeaderboard         = hasLeaderboard
        self.hasDifferentGoals      = hasDifferentGoals
        self.hasWinningCondition    = hasWinningCondition
        self.hasLoosingCondition    = hasLoosingCondition

        #pygame.init()
        self.screen     = pygame.display.set_mode((1280, 720))
        self.clock      = pygame.time.Clock()
        self.running   = True
        self.dt         = 0


        #################################################################################################################################
        ############# GAME SETUP ########################################################################################################
        #################################################################################################################################
        self.center             = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)  
        self.end                = pygame.Vector2(pygame.mouse.get_pos())                              
        self.will_draw_arrow    = False                                                   
        
        # get random vector positions for goalvector
        self.goalVecEndPoint = [pygame.Vector2(random.randint(-5,15),random.randint(-5,15))]

        # FONTS
        self.font  = pygame.font.SysFont('Arial', 8,  bold=True) 
        self.font2 = pygame.font.SysFont('Arial', 12, bold=True) 
        self.font3 = pygame.font.SysFont('Arial', 40, bold=True)
        self.font4 = pygame.font.SysFont('Arial', 16, bold=True)
   
        # TEXT
        self.welcomeText = 'Skapa den svarta vektorn V m.h.a vektoraddition'


        # BUTTON ASSIGNMENT
        self.assignmentButton   = Buttons.Button(screen, self.conv_coord(-10,5).x,   self.conv_coord(-10,5).y,20*20,  10*20,  " ")
        self.projx              = Buttons.Button(screen, self.conv_coord(-28,-11).x, self.conv_coord(-28,-11).y,4*20, 2*20,   'Proj_x(V)')
        self.projy              = Buttons.Button(screen, self.conv_coord(-28,-8).x,  self.conv_coord(-28,-8).y,4*20,  2*20,   'Proj_y(V)')
        self.middleButton       = Buttons.Button(screen, self.conv_coord(-22,-11).x, self.conv_coord(-28,-11).y,4*20, 2*20,   '-V')
        self.rightButton        = Buttons.Button(screen, self.conv_coord(-16,-11).x, self.conv_coord(-28,-11).y,4*20, 2*20,   'Perpj_n(V)')
        self.undo               = Buttons.Button(screen, self.conv_coord(-28,-6).x,  self.conv_coord(-28,-6).y,4*11,  2*11,   'undo')
        self.info               = Buttons.Button(screen, self.conv_coord(-14,-6).x,  self.conv_coord(-14,-6).y,4*7,   2*11,   'info')
        self.nextGame           = Buttons.Button(screen, self.conv_coord(-19,-6).x,  self.conv_coord(-19,-6).y,4*16,  2*11,   'next game')
        
        # LIST OF ALL BUTTONS
        self.allButtons         = [self.middleButton,self.rightButton,self.projx,self.undo,self.projy,self.info,self.nextGame]

        # ARROW AND HISTORY LISTS
        self.goalArrows      = [Arrow.arrow(screen, self.conv_coord(0,0), self.conv_coord(self.goalVecEndPoint[-1].x,self.goalVecEndPoint[-1].y))]
        self.arrowHistory    = list()
        self.last_x          = list()
        self.last_y          = list()
        self.last_x.append(0)
        self.last_y.append(0)

        #### 
        self.winningState   = False 


    def conv_coord(self, x_coord,y_coord):
        '''
        om x_coord = 0 , då är x_conv = screen.width()/2 
        om y_coord = 0, då är y_conv = screen.width()/2

        om x_coord = -20, ?  x_conv= screen.width()/2 + x_coord*delta_x
        '''
        delta_x = 20 
        delta_y = 20
        return pygame.Vector2([(self.screen.get_width()/2 + x_coord*delta_x),(self.screen.get_height()/2 + (-1)*y_coord*delta_y)])

    #################################################################################################################################
    ############# GAME FUNCTIONS ####################################################################################################
    #################################################################################################################################


    def drawGraph(self):
         # Draw x and y lines covering the screen
        delta_y = 0
        i = int(self.screen.get_height()/20/2)
        while (delta_y < self.screen.get_height()):
            
            pygame.draw.lines(self.screen, "gray", False, [(0,delta_y),(self.screen.get_width(),delta_y)], width=1)
            
            img = self.font.render(str(i), True, pygame.Color("black"), pygame.Color("white"))
            if(i!=0):
                self.screen.blit(img, ((self.screen.get_width() - img.get_width())/2-10,(delta_y-img.get_height()/2)))
            
            i-=1
            delta_y+=20 # sets space between lines
        i=int(-1*self.screen.get_width()/20/2)
        delta_x = 0
        while (delta_x < self.screen.get_width()):
            pygame.draw.lines(self.screen, "gray", False, [(delta_x,0),(delta_x,self.screen.get_height())], width=1)
            
            img = self.font.render(str(i), True, pygame.Color("black"), pygame.Color("white"))
            if(i!=0):
                self.screen.blit(img, (delta_x-img.get_width()/2,(self.screen.get_height() - img.get_height())/2+10))
            
            delta_x+=20 # sets space between lines
            i+=1
        #Draw x-axis
        pygame.draw.lines(self.screen, "black", False, [(self.screen.get_width()/2,0),(self.screen.get_width()/2,self.screen.get_height())], width=2)
        #Draw y-axis
        pygame.draw.lines(self.screen, "black", False, [(0,self.screen.get_height()/2),(self.screen.get_width(),self.screen.get_height()/2)], width=2)
   
    def drawInfoButton(self):
        self.assignmentButton.process()
        info1 = self.font4.render("Skapa vektorn V m.h.a vektoraddition", True, "white")
        info2 = self.font2.render("Proj_x(V) = projektionen av V på x axeln", True, "white")
        info3 = self.font2.render("-V = en inverterad vektor V", True, "white")
        info4 = self.font2.render("perpn_j(V) = den vinkelräta projektionen av vektorn V på normalen", True, "white")
        self.screen.blit(info1, self.conv_coord(-9,4))
        self.screen.blit(info2, self.conv_coord(-9,2))
        self.screen.blit(info3, self.conv_coord(-9,0))
        self.screen.blit(info4, self.conv_coord(-9,-2))

    def drawButtons(self):
        pygame.draw.rect(self.screen, "grey", pygame.Rect(self.conv_coord(-30,-13).x, self.conv_coord(-30,-5).y, 20*20, 10*20))
        # if not winningState, draw all buttons, else draw only "next game" button
        if(not self.winningState):
            for button in self.allButtons:
                button.process()
        else: 
            self.allButtons[6].process()

        if(self.allButtons[0].buttonActive): # -V 
            try:
                self.arrowHistory.append(Arrow.arrow(self.screen, self.conv_coord(self.last_x[-1],self.last_y[-1]), self.conv_coord(self.last_x[-1]-(self.goalVecEndPoint[-1].x),self.last_y[-1]-(self.goalVecEndPoint[-1].y))))
                self.last_x.append(self.last_x[-1]-(self.goalVecEndPoint[-1].x))
                self.last_y.append(self.last_y[-1]-(self.goalVecEndPoint[-1].y))
                self.allButtons[0].buttonActive = False # annars spammar den pga man "klickar" 60 ggr / sek
            except AttributeError:
                print('could not add -V')
        if(self.allButtons[1].buttonActive): # perpj_(V)
            try:
                self.arrowHistory.append(Arrow.arrow(self.screen, self.conv_coord(self.last_x[-1],self.last_y[-1]), self.conv_coord(self.last_x[-1],self.last_y[-1]+(self.goalVecEndPoint[-1].y))))
                self.last_x.append(self.last_x[-1])
                self.last_y.append(self.last_y[-1]+(self.goalVecEndPoint[-1].y))
                self.allButtons[1].buttonActive = False # annars spammar den pga man "klickar" 60 ggr / sek
            except AttributeError:
                print('could not add projection of V on x')
        if(self.allButtons[2].buttonActive): # projection of V on x 
            try:
                self.arrowHistory.append(Arrow.arrow(self.screen, self.conv_coord(self.last_x[-1],self.last_y[-1]), self.conv_coord(self.last_x[-1]+(self.goalVecEndPoint[-1].x),self.last_y[-1])))
                self.last_x.append(self.last_x[-1]+(self.goalVecEndPoint[-1].x))
                self.last_y.append(self.last_y[-1])
                self.allButtons[2].buttonActive = False # annars spammar den pga man "klickar" 60 ggr / sek
            except AttributeError:
                print('could not add projection of V on x')
        if(self.allButtons[4].buttonActive): # projection of V on y
            try:
                self.arrowHistory.append(Arrow.arrow(self.screen, self.conv_coord(self.last_x[-1],self.last_y[-1]), self.conv_coord(self.last_x[-1],self.last_y[-1]+(self.goalVecEndPoint[-1].y))))
                self.last_x.append(self.last_x[-1])
                self.last_y.append(self.last_y[-1]+(self.goalVecEndPoint[-1].y))
                self.allButtons[4].buttonActive = False # annars spammar den pga man "klickar" 60 ggr / sek
            except AttributeError:
                print('could not add projection of V on x')
        if(self.allButtons[5].buttonActive): # projection of V on x 
            try:
                self.assignmentButton.buttonActive = False
                self.allButtons[5].buttonActive = False
            except AttributeError:
                print('could press info')
        if(self.allButtons[3].buttonActive and len(self.arrowHistory)>0): # Undo  
            try:
                arrow = self.arrowHistory.pop()
                self.last_x.pop()
                self.last_y.pop()
                self.allButtons[3].buttonActive = False 
            except AttributeError:
                print('could not remove last added arrow')
        if(self.allButtons[6].buttonActive): # next game
            try:
                self.goalVecEndPoint.append(pygame.Vector2(random.randint(-5,15),random.randint(-5,15)))
                self.goalArrows.append(Arrow.arrow(self.screen, self.conv_coord(0,0), self.conv_coord(self.goalVecEndPoint[-1].x,self.goalVecEndPoint[-1].y)))
                self.arrowHistory.clear()
                self.last_x.clear()
                self.last_y.clear()
                self.last_x.append(0)
                self.last_y.append(0)
                self.winningState = False
                self.allButtons[6].buttonActive = False 
            except AttributeError:
                print('could not start next game')

    def drawArrows(self):
        # Draw user arrows
        if(len(self.arrowHistory) > 0):
            for arrow in self.arrowHistory:
                arrow.draw_arrow()

    def drawText(self):
        ## Draw current and goal positions in toolbox 
        posText = "Current position: ("+str(int(self.last_x[-1]))+","+str(int(self.last_y[-1]))+")"
        displayPos = self.font2.render(posText, True, (0, 0, 0))
        self.screen.blit(displayPos, self.conv_coord(-28,-14))
        
        goalPosText = "Goal: ("+str(int(self.goalVecEndPoint[-1].x))+","+str(int(self.goalVecEndPoint[-1].y))+")"
        displayGoalPos = self.font2.render(goalPosText, True, (0, 0, 0))
        self.screen.blit(displayGoalPos, self.conv_coord(-16,-14))
        
        # if current point = goal point success!
        if (int(self.last_x[-1]) == int(self.goalVecEndPoint[-1].x) and int(self.last_y[-1]) == int(self.goalVecEndPoint[-1].y)):
            self.winningState = True
            displayPos = self.font3.render("SUCCESS!", True, (0, 0, 0))
            self.screen.blit(displayPos, self.conv_coord(-5,16))
            statsMessage = "It took you " + str(len(self.arrowHistory))+" steps to win"
            displayStats = self.font2.render(statsMessage, True, (0, 0, 0))
            self.screen.blit(displayStats, self.conv_coord(-27,-8))



    #################################################################################################################################
    ############# GAME LOOP #########################################################################################################
    #################################################################################################################################



    def start(self):
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill("white")
        
            # if treasure hunter game drawMap()
            self.drawGraph()
            
            # either draws info-bubble or buttons, arrows and text
            if(not self.assignmentButton.buttonActive):
                self.drawInfoButton()
            else:
                # Draw latest goal arrow
                self.goalArrows[-1].draw_arrow()

                self.drawButtons()
                self.drawArrows()
                self.drawText()
                # if score
                # if streak
                # if leaderboards
                # if differentGoals
                # if winningCondition
                # if loosingCondition
                
            # fill the screen with a color to wipe away anything from last frame
                  

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = self.clock.tick(60) / 1000

        #if(hasScore):
        #   score() 
        #if(hasStreak)
        #   streak()
        #