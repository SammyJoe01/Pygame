import pygame

#Initialise
pygame.init()

#Surface and Caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
pygame.display.set_caption('Blitting Text')

#Define colors as RGB tuples
BLACK = (0,0,0)
GREEN = (0,255,0)
DARKGREEN = (10,50,10)

#Check Fonts 
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

#Define Fonts 
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font("/Users/sammyjoe/Desktop/UNI/Python/MyPygame/basic_pygame/Graffiti.ttf" , 32)

#Define Text 
system_text = system_font.render('Dragons Rule', True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render('Move the dragon soon!', True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

#Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    #Blit text surface to display surface 
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    #Update display 
    pygame.display.update()


#End Game
pygame.quit()