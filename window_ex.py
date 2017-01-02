import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))

is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            is_blue = not is_blue

        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        
        if event.type == pygame.QUIT:
                
            pygame.quit()
            sys.exit()

        pressed = pygame.key.get_pressed()
        
        if (pressed[pygame.K_UP] or pressed[pygame.K_w]): y -= 3
        if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]): y += 3
        if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]): x -= 3
        if (pressed[pygame.K_RIGHT]or pressed[pygame.K_d]): x += 3

        # Draws a blue/orange rectangle at (x,y) coordinates
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

        pygame.display.flip()
        clock.tick(60)
    
