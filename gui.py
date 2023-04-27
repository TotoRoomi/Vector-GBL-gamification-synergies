import pygame
import random
import Arrow
import Buttons
import time 

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0



# FUNCTIONS 
def conv_coord(x_coord,y_coord):
    '''
    om x_coord = 0 , då är x_conv = screen.width()/2 
    om y_coord = 0, då är y_conv = screen.width()/2

    om x_coord = -20, ?  x_conv= screen.width()/2 + x_coord*delta_x
    '''
    delta_x = 20 
    delta_y = 20
    return pygame.Vector2([(screen.get_width()/2 + x_coord*delta_x),(screen.get_height()/2 + (-1)*y_coord*delta_y)])
    
    

# END OF FUNCTIONS


##############
# GAME SETUP #
##############
center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
end = pygame.Vector2(pygame.mouse.get_pos())
will_draw_arrow = False

# get font object
font = pygame.font.SysFont('Arial', 8, bold=True) 
font2 = pygame.font.SysFont('Arial', 12, bold=True) 
font3 = pygame.font.SysFont('Arial', 40, bold=True) 


# get random vector positions
startPoint = pygame.Vector2(0,0)
goalVecEndPoint = pygame.Vector2(random.randint(-5,15),random.randint(-5,15))
print("goalVecEndPoint is : ",goalVecEndPoint)

x_rand = random.randint(-20,20)
y_rand = random.randint(-15,15)


text = 'Skapa den svarta vektorn V m.h.a vektoraddition'

assignmentButton = Buttons.Button(screen, conv_coord(-30,-5).x, conv_coord(-30,-5).y,20*20, 10*20,text)

projx = Buttons.Button(screen, conv_coord(-28,-11).x, conv_coord(-28,-11).y,4*20,2*20,'Proj_x(V)')

projy = Buttons.Button(screen, conv_coord(-28,-8).x, conv_coord(-28,-8).y,4*20,2*20,'Proj_y(V)')


middleButton = Buttons.Button(screen, conv_coord(-22,-11).x, conv_coord(-28,-11).y,4*20,2*20,'-V')

rightButton = Buttons.Button(screen, conv_coord(-16,-11).x, conv_coord(-28,-11).y,4*20,2*20,'Perpj_n(V)')

undo = Buttons.Button(screen, conv_coord(-28,-7).x, conv_coord(-28,-6).y,4*11,2*11,'undo')


allButtons = [middleButton,rightButton,projx,undo,projy]


testArrow = Arrow.arrow(screen, conv_coord(0,0), conv_coord(goalVecEndPoint.x,goalVecEndPoint.y))

arrowHistory = list()

last_x = list()
last_y = list()
last_x.append(0)
last_y.append(0)

# GAME LOOP
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")


    # Draw x and y lines covering the screen
    delta_y = 0
    i = int(screen.get_height()/20/2)
    while (delta_y < screen.get_height()):
        
        pygame.draw.lines(screen, "gray", False, [(0,delta_y),(screen.get_width(),delta_y)], width=1)
        
        img = font.render(str(i), True, pygame.Color("black"), pygame.Color("white"))
        if(i!=0):
            screen.blit(img, ((screen.get_width() - img.get_width())/2-10,(delta_y-img.get_height()/2)))
        
        i-=1
        delta_y+=20 # sets space between lines
    i=int(-1*screen.get_width()/20/2)
    delta_x = 0
    while (delta_x < screen.get_width()):
        pygame.draw.lines(screen, "gray", False, [(delta_x,0),(delta_x,screen.get_height())], width=1)
        
        img = font.render(str(i), True, pygame.Color("black"), pygame.Color("white"))
        if(i!=0):
            screen.blit(img, (delta_x-img.get_width()/2,(screen.get_height() - img.get_height())/2+10))
        
        delta_x+=20 # sets space between lines
        i+=1
    #Draw x-axis
    pygame.draw.lines(screen, "black", False, [(screen.get_width()/2,0),(screen.get_width()/2,screen.get_height())], width=2)
    #Draw y-axis
    pygame.draw.lines(screen, "black", False, [(0,screen.get_height()/2),(screen.get_width(),screen.get_height()/2)], width=2)

    # Create a list of arrow objects

    # loop thorugh arrow object list and draw them

    # Draw an arrow from origo to the mouse tip
    '''
    if( (not will_draw_arrow) & pygame.mouse.get_pressed()[0]):
        center = pygame.Vector2(pygame.mouse.get_pos())
        will_draw_arrow = True
    if(will_draw_arrow & pygame.mouse.get_pressed()[0]):
        end = pygame.Vector2(pygame.mouse.get_pos())
        #draw_arrow(screen, center, end, pygame.Color("dodgerblue"), 5, 10, 6)
   '''
    
   
   ## TEST
    '''
    # get font object
    font = pygame.font.SysFont('Arial', 12, bold=True)    

    # render a given font into an image
    img = font.render('0', True,
                    pygame.Color("black"),
                    pygame.Color("white"))

    # and finally put it onto the surface.
    # the code below centres text image
    screen.blit(img, ((screen.get_width() - img.get_width())/2,
                    (screen.get_height() - img.get_height())/2))
   '''
   ## TEST 

    #######################
    ##     BUTTONS       ##
    #######################

    if(not assignmentButton.buttonActive):
         assignmentButton.process()
    else:
        pygame.draw.rect(screen, "grey", pygame.Rect(conv_coord(-30,-13).x, conv_coord(-30,-5).y, 20*20, 10*20))
        #draw_arrow(screen, , conv_coord(x_rand,y_rand), pygame.Color("black"), 5, 10, 6)
        testArrow.draw_arrow()
        for button in allButtons:
            button.process()

        if(allButtons[0].buttonActive): # -V 
            try:
                arrowHistory.append(Arrow.arrow(screen, conv_coord(last_x[-1],last_y[-1]), conv_coord(last_x[-1]-(goalVecEndPoint.x),last_y[-1]-(goalVecEndPoint.y))))
                last_x.append(last_x[-1]-(goalVecEndPoint.x))
                last_y.append(last_y[-1]-(goalVecEndPoint.y))
                allButtons[0].buttonActive = False # annars spammar den pga man "klickar" 60 ggr / sek
            except AttributeError:
                print('could not add -V')
        if(allButtons[1].buttonActive): # perpj_(V)
            try:
                arrowHistory.append(Arrow.arrow(screen, conv_coord(last_x[-1],last_y[-1]), conv_coord(last_x[-1],last_y[-1]+(goalVecEndPoint.y))))
                last_x.append(last_x[-1])
                last_y.append(last_y[-1]+(goalVecEndPoint.y))
                allButtons[1].buttonActive = False # annars spammar den pga man "klickar" 60 ggr / sek
            except AttributeError:
                print('could not add projection of V on x')
        if(allButtons[2].buttonActive): # projection of V on x 
            try:
                arrowHistory.append(Arrow.arrow(screen, conv_coord(last_x[-1],last_y[-1]), conv_coord(last_x[-1]+(goalVecEndPoint.x),last_y[-1])))
                last_x.append(last_x[-1]+(goalVecEndPoint.x))
                last_y.append(last_y[-1])
                allButtons[2].buttonActive = False # annars spammar den pga man "klickar" 60 ggr / sek
            except AttributeError:
                print('could not add projection of V on x')
        if(allButtons[4].buttonActive): # projection of V on y
            try:
                arrowHistory.append(Arrow.arrow(screen, conv_coord(last_x[-1],last_y[-1]), conv_coord(last_x[-1],last_y[-1]+(goalVecEndPoint.y))))
                last_x.append(last_x[-1])
                last_y.append(last_y[-1]+(goalVecEndPoint.y))
                allButtons[4].buttonActive = False # annars spammar den pga man "klickar" 60 ggr / sek
            except AttributeError:
                print('could not add projection of V on x')
        if(allButtons[3].buttonActive and len(arrowHistory)>0): # projection of V on x 
            try:
                arrow = arrowHistory.pop()
                last_x.pop()
                last_y.pop()
                allButtons[3].buttonActive = False 
            except AttributeError:
                print('could not remove last added arrow')

        # Draw user arrows
        if(len(arrowHistory) > 0):
            for arrow in arrowHistory:
                arrow.draw_arrow()

        ## Draw current and goal positions in toolbox 
        posText = "Current position: ("+str(int(last_x[-1]))+","+str(int(last_y[-1]))+")"
        displayPos = font2.render(posText, True, (0, 0, 0))
        screen.blit(displayPos, conv_coord(-28,-14))
        
        goalPosText = "Goal: ("+str(int(goalVecEndPoint.x))+","+str(int(goalVecEndPoint.y))+")"
        displayGoalPos = font2.render(goalPosText, True, (0, 0, 0))
        screen.blit(displayGoalPos, conv_coord(-16,-14))
        
        # if current point = goal point success!
        if (int(last_x[-1]) == int(goalVecEndPoint.x) and int(last_y[-1]) == int(goalVecEndPoint.y)):
            displayPos = font3.render("SUCCESS!", True, (0, 0, 0))
            screen.blit(displayPos, conv_coord(-22,-5))
        


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    
    # 

    



pygame.quit()