import pygame

#Initialise
pygame.init()

#Surface and Caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
pygame.display.set_caption('Blitting Images')

#Define colors as RGB tuples
WHITE = (255,255,255) 

#Create Images
dragon_left_image = pygame.image.load("/Users/sammyjoe/Desktop/UNI/Python/MyPygame/basic_pygame/dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,0)


dragon_right_image = pygame.image.load("/Users/sammyjoe/Desktop/UNI/Python/MyPygame/basic_pygame/dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH,0)


#Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 


    #Blit (Copy) surface obj at given coordinates to our display
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    
    pygame.draw.line(display_surface, WHITE, (0,75), (WINDOW_WIDTH,75), 5)
   
    #Update display 
    pygame.display.update()


#End Game
pygame.quit()