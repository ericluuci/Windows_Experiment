# Eric Lu

import pygame
from pygame import *
import sys


class GameApp:

    def __init__(self):

        # Creates window and title
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('##GAME## - Eric Lu')

        # Loads music
        pygame.mixer.music.load('background.mp3')
        pygame.mixer.music.play(-1)

        # Loads background image
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (800, 600))
        self.screen.blit(self.bg, (0,0))

        clock = pygame.time.Clock()
        clock.tick(60)

    def mainloop(self):

        while True:

            for e in pygame.event.get():

                if (e.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                if (e.type == KEYDOWN and (e.key == K_RIGHT or e.key == K_d)):
                    pass

                if (e.type == KEYDOWN and (e.key == K_LEFT or e.key == K_a)):
                    pass

                if (e.type == KEYDOWN and (e.key == K_UP or e.key == K_w)):
                    pass

                if (e.type == KEYDOWN and (e.key == K_DOWN or e.key == K_s)):
                    pass

        pygame.display.update() 

if __name__ == '__main__':
    GameApp().mainloop()
