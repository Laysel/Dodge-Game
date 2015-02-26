import pygame, os, random
from pygame.locals import *

car_img = os.path.join('C:\Python33\Dodge\images', 'car.png')

class Car(object):

    def __init__(self):
        self.image = pygame.image.load(car_img)
        self.x = 390
        self.y = 450

    def movement(self):
        key = pygame.key.get_pressed()
        distance = 5
        if key[pygame.K_DOWN]:
            self.y += distance
        elif key[pygame.K_UP]:
            self.y -= distance
        elif key[pygame.K_RIGHT]:
            self.x += distance
        elif key[pygame.K_LEFT]:
            self.x -= distance

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        
def main():
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    white = (255,255,255)
    
    car = Car()
    clock = pygame.time.Clock()
    
    background = pygame.image.load('images/game_bg.png')
    enemy_img = pygame.image.load('images/enemy.png')

    def enemycar(enemyx, enemyy):
        screen.blit(enemy_img, (enemyx, enemyy))

    enemycar_startx = random.randrange(0, 800)
    enemycar_starty = -600
    enemycar_speed = 10

    running = True
    
    while running:
        
        screen.fill(0)
        screen.blit(background,(0,0))
        
        car.movement()
        car.draw(screen)
        
        enemycar(enemycar_startx, enemycar_starty)
        enemycar_starty += enemycar_speed

        pygame.display.flip()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        clock.tick(40)

if __name__=='__main__':
    main()
