import pygame

#Initialise
pygame.init()

#Surface and Caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
pygame.display.set_caption('Discrete Movement')

#Set game values
VELOCITY = 50

#Load Images
dragon_image = pygame.image.load("/Users/sammyjoe/Desktop/UNI/Python/MyPygame/basic_pygame/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH//2
dragon_rect.bottom = WINDOW_HEIGHT


#Loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False 

        #Check for discrete movement 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY


    #Clear screen before moving 
    display_surface.fill((0,0,0))

    #Blit assets to screen
    display_surface.blit(dragon_image, dragon_rect)

    #Update display 
    pygame.display.update()


#End Game
pygame.quit()