
import pygame
import random
import Arrow
import Buttons

class gameloop():
    def __init__(self,screen,hasScore, hasStreak,hasLeaderboard, hasDifferentGoals,hasWinningCondition,hasLoosingCondition):
        
        self.screen                 = screen
        self.hasScore               = hasScore
        self.hasStreal              = hasStreak
        self.hasLeaderboard         = hasLeaderboard
        self.hasDifferentGoals      = hasDifferentGoals
        self.hasWinningCondition    = hasWinningCondition
        self.hasLoosingCondition    = hasLoosingCondition

        #pygame.init()
        self.screen     = pygame.display.set_mode((1280, 720))
        self.clock      = pygame.time.Clock()
        #self.running   = True
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
        self.assignmentButton   = Buttons.Button(screen, conv_coord(-10,5).x,   conv_coord(-10,5).y,20*20,  10*20,  " ")
        self.projx              = Buttons.Button(screen, conv_coord(-28,-11).x, conv_coord(-28,-11).y,4*20, 2*20,   'Proj_x(V)')
        self.projy              = Buttons.Button(screen, conv_coord(-28,-8).x,  conv_coord(-28,-8).y,4*20,  2*20,   'Proj_y(V)')
        self.middleButton       = Buttons.Button(screen, conv_coord(-22,-11).x, conv_coord(-28,-11).y,4*20, 2*20,   '-V')
        self.rightButton        = Buttons.Button(screen, conv_coord(-16,-11).x, conv_coord(-28,-11).y,4*20, 2*20,   'Perpj_n(V)')
        self.undo               = Buttons.Button(screen, conv_coord(-28,-6).x,  conv_coord(-28,-6).y,4*11,  2*11,   'undo')
        self.info               = Buttons.Button(screen, conv_coord(-14,-6).x,  conv_coord(-14,-6).y,4*7,   2*11,   'info')
        self.nextGame           = Buttons.Button(screen, conv_coord(-19,-6).x,  conv_coord(-19,-6).y,4*16,  2*11,   'next game')
        
        # LIST OF ALL BUTTONS
        self.allButtons         = [self.middleButton,self.rightButton,self.projx,self.undo,self.projy,self.info,self.nextGame]

        # ARROW AND HISTORY LISTS
        self.goalArrows      = [Arrow.arrow(screen, conv_coord(0,0), conv_coord(goalVecEndPoint[-1].x,goalVecEndPoint[-1].y))]
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
        return pygame.Vector2([(screen.get_width()/2 + x_coord*delta_x),(screen.get_height()/2 + (-1)*y_coord*delta_y)])
    
    def start(self):
        #if(hasScore):
        #   score() 
        #if(hasStreak)
        #   streak()
        #