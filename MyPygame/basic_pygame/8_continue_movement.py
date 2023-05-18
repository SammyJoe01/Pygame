import pygame

#Initialise
pygame.init()

#Surface and Caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
pygame.display.set_caption('Continue Movement')

#Define Clock and FPS
FPS = 60
clock = pygame.time.Clock()

#Set game values 
VELOCITY = 5 

#Load Images
dragon_image = pygame.image.load("/Users/sammyjoe/Desktop/UNI/Python/MyPygame/basic_pygame/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


#Loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False 

    #Get list all keys beign pressed down
    keys = pygame.key.get_pressed()
    print(keys)

    #Move dragon continuosly and stop it at the boders of the screen
    if keys[pygame.K_LEFT] and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY
    if keys[pygame.K_UP] and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
        
   
    #Clear screen before moving 
    display_surface.fill((0,0,0))

    #Blit assets to screen
    display_surface.blit(dragon_image, dragon_rect)

    #Update display 
    pygame.display.update()

    #Tick the clock 
    clock.tick(FPS)

#End Game
pygame.quit()