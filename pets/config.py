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

# Font
pygame.font.init()
dogica = pygame.font.Font('./assets/dogica.ttf', 12)
minecraft = pygame.font.Font('./assets/minecraft.ttf', 12)

# Track if the cat sound or food demand has been shown
cat_message_shown = False
cat_message = ''
cat_last_selected = -1  # To track the last selected "Obakeneko" message
