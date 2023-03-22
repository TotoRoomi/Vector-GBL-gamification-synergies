# Example file showing a circle moving on screen
import pygame
from arrow import draw_arrow

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
end = pygame.Vector2(pygame.mouse.get_pos())
will_draw_arrow = False

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
    while (delta_y < screen.get_height()):
        pygame.draw.lines(screen, "gray", False, [(0,delta_y),(screen.get_width(),delta_y)], width=1)
        delta_y+=10
    delta_x = 0
    while (delta_x < screen.get_width()):
        pygame.draw.lines(screen, "gray", False, [(delta_x,0),(delta_x,screen.get_height())], width=1)
        delta_x+=10
    
    #Draw x-axis
    pygame.draw.lines(screen, "black", False, [(screen.get_width()/2,0),(screen.get_width()/2,screen.get_height())], width=2)
    #Draw y-axis
    pygame.draw.lines(screen, "black", False, [(0,screen.get_height()/2),(screen.get_width(),screen.get_height()/2)], width=2)


    # Draw an arrow from origo to the mouse tip
    if( (not will_draw_arrow) & pygame.mouse.get_pressed()[0]):
        center = pygame.Vector2(pygame.mouse.get_pos())
        will_draw_arrow = True
    if(will_draw_arrow & pygame.mouse.get_pressed()[0]):
        end = pygame.Vector2(pygame.mouse.get_pos())
        draw_arrow(screen, center, end, pygame.Color("dodgerblue"), 10, 20, 12)
   

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


    # 

pygame.quit()