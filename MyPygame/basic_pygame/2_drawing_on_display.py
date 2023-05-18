import pygame

#Initialise
pygame.init()

#Surface and Caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
pygame.display.set_caption('Drawing Objects')

#Define colors as RGB tuples
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

#Background color
display_surface.fill(BLUE)

#Draw shapes 
#Line(Surface,color,starting and ending point, thickness)
pygame.draw.line(display_surface, RED, (0,0), (100,100), 5)
pygame.draw.line(display_surface, GREEN, (100,100), (200,300), 1)

#Circle(Surface,color,center,radius,thickness)
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200,6)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 195,0)

#Rectangles(Surface, color, (top-left x, to-left y, width, height))
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50, 100))

#Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    #Update display 
    pygame.display.update()


#End Game
pygame.quit()