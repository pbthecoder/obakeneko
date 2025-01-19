import pygame, time, random
from config import *

# Main loop
johnson = True
while johnson:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            johnson = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and screen == 'room':
                selected -= 1
                selected = abs(selected % 6)

            if event.key == pygame.K_d and screen == 'room':
                selected += 1
                selected = abs(selected % 6)

            # Check for 'E' key to change background to cardboard box interior
            if event.key == pygame.K_e and screen == 'room':
                screen = 'box'

    # Background handling
    if screen == 'table':
        background = pygame.image.load('./assets/tablebg.png')
        background = pygame.transform.scale(background, (128, 128))  # Resize from 32x32 to 128x128
    elif screen == 'box':
        background = pygame.image.load('./assets/boxbg.png')
        background = pygame.transform.scale(background, (128, 128))  # Resize from 32x32 to 128x128
    elif screen == 'outside':
        background = pygame.image.load('./assets/outsidebg.png')
        background = pygame.transform.scale(background, (128, 128))  # Resize from 32x32 to 128x128
    elif screen == 'flowers':
        background = pygame.image.load('./assets/flowersbg.png')
        background = pygame.transform.scale(background, (128, 128))  # Resize from 32x32 to 128x128
    elif screen == 'tv':
        background = pygame.image.load('./assets/tvbg.png')
        background = pygame.transform.scale(background, (128, 128))  # Resize from 32x32 to 128x128
    else:
        background = pygame.image.load('./assets/tatamihomebg.png')
        background = pygame.transform.scale(background, (128, 128))  # Resize from 32x32 to 128x128

    if selected == 0 and screen == 'room':  # Selected cat
        arrow_x = 50
        arrow_y = 71
        arrow = pygame.image.load('./assets/arrowleft.png')
        write("Obakeneko\n*nya!", (255, 255, 255), (0, 0, 0), 0, 104)

    elif selected == 1 and screen == 'room':  # Selected Table
        arrow_x = 80
        arrow_y = 56
        arrow = pygame.image.load('./assets/arrowleft.png')
        write('Table\nThe tea is cold.', (255, 255, 255), (0, 0, 0), 0, 104)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and screen == 'room':
                    screen = 'table'
    elif selected == 2 and screen == 'room':  # Selected Flowers
        arrow_x = 35
        arrow_y = 31
        arrow = pygame.image.load('./assets/arrowleft.png')
        write('Jacarandas\nThey\'re in season.', (255, 255, 255), (0, 0, 0), 0, 104)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and screen == 'room':
                    screen = 'flowers'
    elif selected == 3 and screen == 'room':  # Selected Outside
        arrow_x = 54
        arrow_y = -4
        arrow = pygame.image.load('./assets/arrowdown.png')
        write('Outside\nIt\'s a full moon.', (255, 255, 255), (0, 0, 0), 0, 104)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and screen == 'room':
                    screen = 'outside'
    elif selected == 4 and screen == 'room':  # Selected TV
        arrow_x = 65
        arrow_y = 26
        arrow = pygame.image.load('./assets/arrowright.png')
        write('Television\nThere\'s a fish.', (255, 255, 255), (0, 0, 0), 0, 104)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and screen == 'room':
                    screen = 'tv'
    elif selected == 5 and screen == 'room':  # Selected Box
        arrow_x = 70
        arrow_y = 81
        arrow = pygame.image.load('./assets/arrowright.png')
        write('Cardboard Box\nHow do cats fit in?', (255, 255, 255), (0, 0, 0), 0, 104)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and screen == 'room':
                    screen = 'box'

    canvas.blit(background, (0, -24))

    if selected == 1 and tabley == -24 and screen == 'room':
        canvas.blit(table, (0, -19))
        tabley = -19
    elif selected != 1 and tabley == -19 and screen == 'room':
        canvas.blit(table, (0, -24))
        tabley = -24
    else:
        canvas.blit(table, (0, -24))
        tabley = -24

    if selected == 2 and flowersy == -24 and screen == 'room':
        canvas.blit(flowers, (0, -19))
        flowersy = -19
    elif selected != 1 and flowersy == -19 and screen == 'room':
        canvas.blit(flowers, (0, -24))
        flowersy = -24
    else:
        canvas.blit(flowers, (0, -24))
        flowersy = -24

    if selected == 4 and tvy == -24 and screen == 'room':
        canvas.blit(tv, (0, -19))
        tvy = -19
    elif selected != 1 and tvy == -19 and screen == 'room':
        canvas.blit(tv, (0, -24))
        tvy = -24
    else:
        canvas.blit(tv, (0, -24))
        tvy = -24

    if selected == 5 and boxy == -30 and screen == 'room':
        canvas.blit(box, (0, -25))
        boxy = -25
    elif selected != 1 and boxy == -25 and screen == 'room':
        canvas.blit(box, (0, -30))
        boxy = -30
    else:
        canvas.blit(box, (0, -30))
        boxy = -30

    if selected == 0 and catx == 6 and caty == 56 and screen == 'room':
        canvas.blit(character, (6, 51))
        catx, caty = 6, 51
    elif selected != 0 and catx == 6 and caty == 51 and screen == 'room':
        canvas.blit(character, (6, 56))
        catx, caty = 6, 56
    else:
        canvas.blit(character, (6, 56))
        catx, caty = 6, 56
    
    canvas.blit(arrow, (arrow_x, arrow_y))

    pygame.display.flip()
    time.sleep(0.5)  # Delay for frame refresh

pygame.quit()
