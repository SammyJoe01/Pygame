import pygame

#Initialise
pygame.init()

#Surface and Caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
pygame.display.set_caption('Adding Sounds')

#Load Sounds 
sound_1 = pygame.mixer.Sound("/Users/sammyjoe/Desktop/UNI/Python/MyPygame/basic_pygame/sound_1.wav")
sound_2 = pygame.mixer.Sound("/Users/sammyjoe/Desktop/UNI/Python/MyPygame/basic_pygame/sound_2.wav")

#Play 
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

#Change volume 
sound_2.set_volume(.1)
sound_2.play()
pygame.time.delay(2000)

#Load background music 
pygame.mixer.music.load("/Users/sammyjoe/Desktop/UNI/Python/MyPygame/basic_pygame/music.wav")

#Play and stop music 
pygame.mixer.music.play(-1)
pygame.time.delay(1000)
sound_1.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

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