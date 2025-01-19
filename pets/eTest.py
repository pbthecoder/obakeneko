import pygame

pygame.init()
canvas = pygame.display.set_mode((128,128))
pygame.display.set_caption('test for E')
johnson = True
while johnson:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            johnson = False

        # Check for 'E' key to change screens
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            print('e pressed')
