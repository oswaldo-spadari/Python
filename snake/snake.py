import pygame, random
from pygame.locals import *


def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')


snake = [(200,200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,0,0))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font(freesansbold.ttf, 18)
score = 0

game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.fill((0,0,0))

    pygame.display.update()
