import pygame

#Initialise
pygame.init()

#Surface and Caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
pygame.display.set_caption('Mouse Movement')

#Load Images
dragon_image = pygame.image.load("/Users/sammyjoe/Desktop/UNI/Python/MyPygame/basic_pygame/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)


#Loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False 

        #Move based on mouse clicks 
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y

        #Click and hold to follow the mouse 
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y
   
    #Clear screen before moving 
    display_surface.fill((0,0,0))

    #Blit assets to screen
    display_surface.blit(dragon_image, dragon_rect)

    #Update display 
    pygame.display.update()

#End Game
pygame.quit()