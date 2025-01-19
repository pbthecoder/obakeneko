import pygame, time, random
pygame.init()

canvas = pygame.display.set_mode((128, 128))
pygame.display.set_caption("obakeneko.ogg")

# Functions
def write(towrite, textcolor, highlight, x, y):
    lines = towrite.split('\n')
    canvas.fill(highlight, (x, y, 128, 128))
    for i, line in enumerate(lines):
        text = minecraft.render(line, True, textcolor)
        textw, texth = text.get_size()
        canvas.blit(text, (x, y + i * texth))

# Asset Images
character = pygame.image.load('./assets/neko.gif')
character = pygame.transform.scale(character, (48, 48))  # Resize from 64x64 to 48x48
character = pygame.transform.flip(character, True, False)  # Flip horizontal
catx, caty = 6, 68

background = pygame.image.load('./assets/tatamihomebg.png')
background = pygame.transform.scale(background, (128, 128))  # Resize from 32x32 to 128x128

table = pygame.image.load('./assets/table.png')
table = pygame.transform.scale(table, (128, 128))  # Resize from 32x32 to 128x128
tabley = 0

tv = pygame.image.load('./assets/tv.png')
tv = pygame.transform.scale(tv, (128, 128))  # Resize from 32x32 to 128x128
tvy = 0

flowers = pygame.image.load('./assets/flowers.png')
flowers = pygame.transform.scale(flowers, (128, 128))  # Resize from 32x32 to 128x128
flowersy = 0

box = pygame.image.load('./assets/box.png')
box = pygame.transform.scale(box, (128, 128))  # Resize from 32x32 to 128x128
boxy = 0

arrow = pygame.image.load('./assets/arrowright.png')
selected = 0
arrow_x = 0
arrow_y = 0

# Misc. variables
screen = 'room'
hunger = 0
boredom = 0
love = 5
catsounds = ['*meow!', '*nya!', '*purr!', '*hiss!', '*puru.',
             '*miaou!', '*nyaaaa!', '*unya-unya!', '*chuu-chuu.',
             'It demands churu.', 'It demands tuna.', 'It demands chicken.',
             'It demands meat sticks.', 'It demands bonito.']

# Font
pygame.font.init()
dogica = pygame.font.Font('./assets/dogica.ttf', 12)
minecraft = pygame.font.Font('./assets/minecraft.ttf', 12)

# Track if the cat sound or food demand has been shown
cat_message_shown = False
cat_message = ''

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

    if selected == 0:  # Selected cat
        arrow_x = 50
        arrow_y = 71
        arrow = pygame.image.load('./assets/arrowleft.png')

        # Only show the cat message if it hasn't been shown already
        if not cat_message_shown:
            # Random delay before showing the message
            cat_message = 'Obakeneko\n' + random.choice(catsounds)
            cat_message_shown = True

        # Display the cat message
        write(cat_message, (255, 255, 255), (0, 0, 0), 0, 104)

    elif selected == 1:  # Selected Table
        arrow_x = 80
        arrow_y = 56
        arrow = pygame.image.load('./assets/arrowleft.png')
        write('Table\nThe tea is cold.', (255, 255, 255), (0, 0, 0), 0, 104)
    elif selected == 2:  # Selected Flowers
        arrow_x = 35
        arrow_y = 31
        arrow = pygame.image.load('./assets/arrowleft.png')
        write('Jacarandas\nThey\'re in season.', (255, 255, 255), (0, 0, 0), 0, 104)
    elif selected == 3:  # Selected Outside
        arrow_x = 54
        arrow_y = -4
        arrow = pygame.image.load('./assets/arrowdown.png')
        write('Outside\nIt\'s a full moon.', (255, 255, 255), (0, 0, 0), 0, 104)
    elif selected == 4:  # Selected TV
        arrow_x = 65
        arrow_y = 26
        arrow = pygame.image.load('./assets/arrowright.png')
        write('Television\nThere\'s a fish.', (255, 255, 255), (0, 0, 0), 0, 104)
    elif selected == 5:  # Selected Box
        arrow_x = 70
        arrow_y = 81
        arrow = pygame.image.load('./assets/arrowright.png')
        write('Cardboard Box\nHow do cats fit in?', (255, 255, 255), (0, 0, 0), 0, 104)

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

    canvas.blit(background, (0, -24))

    if selected == 1 and tabley == -24:
        canvas.blit(table, (0, -19))
        tabley = -19
    elif selected != 1 and tabley == -19:
        canvas.blit(table, (0, -24))
        tabley = -24
    else:
        canvas.blit(table, (0, -24))
        tabley = -24

    if selected == 2 and flowersy == -24:
        canvas.blit(flowers, (0, -19))
        flowersy = -19
    elif selected != 1 and flowersy == -19:
        canvas.blit(flowers, (0, -24))
        flowersy = -24
    else:
        canvas.blit(flowers, (0, -24))
        flowersy = -24

    if selected == 4 and tvy == -24:
        canvas.blit(tv, (0, -19))
        tvy = -19
    elif selected != 1 and tvy == -19:
        canvas.blit(tv, (0, -24))
        tvy = -24
    else:
        canvas.blit(tv, (0, -24))
        tvy = -24

    if selected == 5 and boxy == -30:
        canvas.blit(box, (0, -25))
        boxy = -25
    elif selected != 1 and boxy == -25:
        canvas.blit(box, (0, -30))
        boxy = -30
    else:
        canvas.blit(box, (0, -30))
        boxy = -30

    if selected == 0 and catx == 6 and caty == 56:
        canvas.blit(character, (6, 51))
        catx, caty = 6, 51
    elif selected != 0 and catx == 6 and caty == 51:
        canvas.blit(character, (6, 56))
        catx, caty = 6, 56
    else:
        canvas.blit(character, (6, 56))
        catx, caty = 6, 56

    canvas.blit(arrow, (arrow_x, arrow_y))

    pygame.display.flip()
    time.sleep(0.5)  # Delay for frame refresh
pygame.quit()
