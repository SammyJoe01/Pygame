import pygame, random 

#Initialise pygame
pygame.init()

#Create a display surface and set its caption
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Collision Detection')

#Set FPS and Clock 
FPS = 60 
clock = pygame.time.Clock()

#Set game values 
VELOCITY = 5 

#Load Images
dragon_image = pygame.image.load("/Users/sammyjoe/Desktop/UNI/Python/MyPygame/basic_pygame/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)

coin_image = pygame.image.load("/Users/sammyjoe/Desktop/UNI/Python/MyPygame/basic_pygame/coin.png")
coin_rect = dragon_image.get_rect()
coin_rect.center = (WINDOW_HEIGHT//2, WINDOW_WIDTH//2)


#Main game loop
running = True
while running:
    #Loop trough a list of event objects that have occured 
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


    #Draw rectangles to represent objects
    dragon_rect_surface = pygame.Surface((dragon_rect.width, dragon_rect.height), pygame.SRCALPHA)
    coin_rect_surface = pygame.Surface((coin_rect.width, coin_rect.height), pygame.SRCALPHA)

    #Check for collision
    if dragon_rect.colliderect(coin_rect):
        print('HIT')
        coin_rect.x = random.randint(0, WINDOW_WIDTH -32)
        coin_rect.y = random.randint(0, WINDOW_HEIGHT -32)

    #Blit assets to screen
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)

    #Update display 
    pygame.display.update()

    #Tick the clock 
    clock.tick(FPS)

#End Game
pygame.quit()