import pygame, os, random
from pygame.locals import *

def main():

    pygame.init()

    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('DODGE')
    bg = pygame.image.load('game_images/game_bg2.png')
    enemyImg = pygame.image.load('game_images/enemy2.png')
    playerImg = pygame.image.load('game_images/car.png')
    startpos = [375, 480]
    white = (255, 255, 255)
    score = 0
    clock = pygame.time.Clock()
    
    frame_count = 0
    frame_rate = 40
    start_time = 90

    timer = 100
    timer1 = 0
    enemies = [[800, 600]]
    
    def dodged_score(count):
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("Score : "+str(count), True, white)
        screen.blit(text, (60,0))

    crashed = False

    while not crashed:

        timer -= 1
        
        #add enemies
        if timer == 0:
            enemies.append([random.randint(50, 610), 0])
            timer = 100 - (timer1 * 2)
            if timer1 >= 35:
                timer1 = 35
            else:
                timer1 += 5
        index = 0
        for enemy in enemies:
            if enemy[0] > 600:
                enemies.pop(index)
                score += 1
            enemy[1] += 7
            index += 1
            
        #timer
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0

        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
        
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render(output_string, True, white)
        
        #player movement
        key = pygame.key.get_pressed()
        distance = 15
        if key[pygame.K_DOWN]:
            startpos[1] += distance
        elif key[pygame.K_UP]:
            startpos[1] -= distance
        elif key[pygame.K_RIGHT]:
            startpos[0] += distance
        elif key[pygame.K_LEFT]:
            startpos[0] -= distance
        
        #update screen      
        screen.fill(0)
        screen.blit(bg, (0,0))
        screen.blit(text, (570,0))
        screen.blit(playerImg, startpos)
        dodged_score(score)

        for enemy in enemies:
            screen.blit(enemyImg, enemy)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                crashed = True

        frame_count += 1
        clock.tick(frame_rate)

if __name__ == '__main__':
    main()