import pygame
import random

pygame.init()

height = 800
width = 600

screen = pygame.display.set_mode((height, width))
clock = pygame.time.Clock()
pygame.display.set_caption("JOGO DO MONSTRO - INÁCIO AMERIO")

class Player(object):
        
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

        self.playerFront = True
        self.playerBack = False
        
        self.spriteFront = pygame.image.load('PLAYER_FRONT.png')
        self.spriteBack = pygame.image.load('PLAYER_BACK.png')

class Monster(object):
        
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1
        
        self.spriteSpawn = pygame.image.load('MONSTER.png')

class Gold(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.hasGold = False
        
        self.spriteSpawn = pygame.image.load('OURO_SPAWN.png')
        self.spriteDespawn = pygame.image.load('OURO_DESPAWN.png')

class Exit(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.spriteSpawn = pygame.image.load('EXIT.png')

class Hole(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.spriteSpawn = pygame.image.load('HOLE.png')

player = Player(5, 560, 32, 32)
monster1 = Monster(random.randrange(0, 781, 5), random.randrange(0, 551, 5), 32, 32)
monster2 = Monster(random.randrange(0, 781, 5), random.randrange(0, 551, 5), 32, 32)
monster3 = Monster(random.randrange(0, 781, 5), random.randrange(0, 551, 5), 32, 32)

hole1 = Hole(random.randrange(0, 781, 5), random.randrange(0, 551, 5), 32, 32)
hole2 = Hole(random.randrange(0, 781, 5), random.randrange(0, 551, 5), 32, 32)
hole3 = Hole(random.randrange(0, 781, 5), random.randrange(0, 551, 5), 32, 32)

gold = Gold(random.randrange(0, 781, 5), random.randrange(0, 551, 5), 32, 32)
exit = Exit(5, 535, 32, 32)

done = False
while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > 5:
        player.x -= player.vel
    if keys[pygame.K_RIGHT] and player.x < 765:
        player.x += player.vel
    if keys[pygame.K_UP] and player.y > 5:
        player.y -= player.vel
        player.playerFront = False
        player.playerBack = True
    if keys[pygame.K_DOWN] and player.y < 560:
        player.y += player.vel
        player.playerBack = False
        player.playerFront = True

    
#   .   .   .   MONSTER 1 MOVEMENT
    if monster1.x > player.x:
        monster1.x -= monster1.vel
    elif monster1.x < player.x:
        monster1.x += monster1.vel

    if monster1.y > player.y:
        monster1.y -= monster1.vel
    elif monster1.y < player.y:
        monster1.y += monster1.vel

#   .   .   .   MONSTER 2 MOVEMENT
    if monster2.x > player.x:
        monster2.x -= monster2.vel
    elif monster2.x < player.x:
        monster2.x += monster2.vel

    if monster2.y > player.y:
        monster2.y -= monster2.vel
    elif monster2.y < player.y:
        monster2.y += monster2.vel

#   .   .   .   MONSTER 3 MOVEMENT
    if monster3.x > player.x:
        monster3.x -= monster3.vel
    elif monster3.x < player.x:
        monster3.x += monster3.vel

    if monster3.y > player.y:
        monster3.y -= monster3.vel
    elif monster3.y < player.y:
        monster3.y += monster3.vel

#   .   .   .   COLISSION CHECK
    if (gold.hasGold == False and (player.x == gold.x and player.y == gold.y)):
        print("Gold")
        gold.hasGold = True

    if (gold.hasGold == True and (player.x == exit.x and player.y == exit.y)):
        done = True

    if (monster1.x == player.x and monster1.y == player.y) or (monster2.x == player.x and monster2.y == player.y) or (monster3.x == player.x and monster3.y == player.y):
        done = True

    if (hole1.x == player.x and hole1.y == player.y) or (hole2.x == player.x and hole2.y == player.y) or (hole3.x == player.x and hole3.y == player.y):
        done = True

    screen.fill((57, 6, 9))

#   .   .   .   CHECKS FOR DRAW IMAGES
    if gold.hasGold == False:
        screen.blit(gold.spriteSpawn, (gold.x, gold.y))

    if gold.hasGold == True:
        screen.blit(gold.spriteDespawn, (gold.x, gold.y))

    if player.playerFront == True:
        screen.blit(player.spriteFront, (player.x, player.y))

    if player.playerBack == True:
        screen.blit(player.spriteBack, (player.x, player.y))

    
    screen.blit(monster1.spriteSpawn, (monster1.x, monster1.y))
    screen.blit(monster2.spriteSpawn, (monster2.x, monster2.y))
    screen.blit(monster3.spriteSpawn, (monster3.x, monster3.y))

    screen.blit(hole1.spriteSpawn, (hole1.x, hole1.y))
    screen.blit(hole2.spriteSpawn, (hole2.x, hole2.y))
    screen.blit(hole3.spriteSpawn, (hole3.x, hole3.y))
    
    screen.blit(exit.spriteSpawn, (exit.x, exit.y))    
    pygame.display.update()

pygame.quit()


