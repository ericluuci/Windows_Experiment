# Eric Lu

import pygame
from pygame import *
import sys

def main():

    up = False
    down = False
    left = False
    right = False

    # Create a sprite group
    entities = pygame.sprite.Group()

    # Adds player to the group
    player = Player(495, 295, 10)
    entities.add(player)

    # Creates window and title
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('##GAME## - Eric Lu')

    # Loads background image
    bg = pygame.image.load('background.jpg')
    bg = pygame.transform.scale(bg, (800, 600))

    # Creates clock
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for e in pygame.event.get():

            if (e.type == QUIT):
                pygame.quit()
                sys.exit()


            if (e.type == KEYDOWN and (e.key == K_UP or e.key == K_w)):
                up = True

            if (e.type == KEYDOWN and (e.key == K_DOWN or e.key == K_s)):
                down = True

            if (e.type == KEYDOWN and (e.key == K_LEFT or e.key == K_a)):
                left =  True

            if (e.type == KEYDOWN and (e.key == K_RIGHT or e.key == K_d)):
                right = True
                

            if (e.type == KEYUP and (e.key == K_UP or e.key == K_w)):
                up = False

            if (e.type == KEYUP and (e.key == K_DOWN or e.key == K_s)):
                down = False

            if (e.type == KEYUP and (e.key == K_LEFT or e.key == K_a)):
                left = False

            if (e.type == KEYUP and (e.key == K_RIGHT or e.key == K_d)):
                right = False

        # Draw background    
        screen.blit(bg, (0, 0))

        # Update sprites
        for sprite in entities:
            sprite.update()

        # Draw sprites
        entities.draw(screen)

        # Update screen
        pygame.display.update()
            
                

class Entity(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)

class Player(Entity):

    def __init__(self, x, y, side):

        Entity.__init__(self)
        self.image_base = pygame.image.load('character.jpg')
        self.rect = Rect(x, y, side, side)

        self.rect.x = x
        self.rect.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.side = side

    def update():

        pass

if __name__ == '__main__':
    main()
