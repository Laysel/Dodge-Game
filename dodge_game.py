import pygame, os, random
from pygame.locals import *

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
    
def quit_game():
    pygame.quit()
    quit()

def main():

    pygame.init()
    pygame.font.init()

    width = 800
    height = 600
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('DODGE')
    
    bg = pygame.image.load('game_images/game_bg2.png')
    enemyImg = pygame.image.load('game_images/enemy2.png')
    playerImg = pygame.image.load('game_images/car.png')
    TUImg = pygame.image.load('game_images/tu.png')
    
    black = (0, 0 , 0)
    white = (255, 255, 255)
    red = (255, 0, 0 )
    green = (0, 200, 0)
    
    score = 0
    startpos = [375, 480]
    player_width = 60
    timer = 100
    timer1 = 0
    enemies = [[800, 600]]
    distance = 50
    clock = pygame.time.Clock()
    
    frame_count = 0
    frame_rate = 40
    start_time = 90

    def score_count(count):
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render("Score : "+str(count), True, white)
        screen.blit(text, (60,0))

    gameExit = False

    while not gameExit:
        pygame.font.init()
        timer -= 1
        
        #timer
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0

        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
        
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render(output_string, True, white)
        
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
                score += 1 #adding the score
            enemy[1] += 7
            index += 1
            
        #collision between cars
        enemyRect = enemyImg.get_rect()
        enemyRect.top = enemy[1] - 10
        enemyRect.left = enemy[0]
        enemyRect.right = enemy[0]
        
        playerRect = playerImg.get_rect()
        playerRect.top = startpos[1]
        playerRect.left = startpos[0]
        playerRect.right = startpos[0]
        
        if enemyRect.colliderect(playerRect):
            font = pygame.font.SysFont("comicsansms", 115)
            text = font.render("You crashed!", True, red)
            screen.blit(text, (60, 200))
            
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                
                mouse1 = pygame.mouse.get_pos()
                click1 = pygame.mouse.get_pressed()
                
                pygame.draw.rect(screen, green, (150, 450, 100, 50))
                smallText1 = pygame.font.SysFont("comicsansms", 20)
                textSurf1, textRect1 = text_objects("Retry", smallText1)
                textRect1.center = ((150 + (100/2)), (450 + (50/2)))
                screen.blit(textSurf1, textRect1)

                if 250 > mouse1[0] > 150 and 500 > mouse1[1] > 450 and click1[0] == 1:
                    main()

                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                pygame.draw.rect(screen, red, (550, 450, 100, 50))
                smallText = pygame.font.SysFont("comicsansms", 20)
                textSurf, textRect = text_objects("Quit", smallText)
                textRect.center = ((550 + (100/2)), (450 + (50/2)))
                screen.blit(textSurf, textRect)

                if 650 > mouse[0] > 550 and 500 > mouse[1] > 450 and click[0] == 1:
                    quit_game()
                    
                pygame.display.update()      
            
            #collision with wall
            if startpos[0] > width - player_width or startpos[0] < 0:
            font = pygame.font.SysFont("comicsansms", 115)
            text = font.render("You crashed!", True, red)
            screen.blit(text, (60, 200))
                
            while True:           
                for event in pygame.event.get():
                       if event.type == pygame.QUIT:
                           pygame.quit()
                           quit()
                           
                mouse1 = pygame.mouse.get_pos()
                click1 = pygame.mouse.get_pressed()
                
                pygame.draw.rect(screen, green, (150, 450, 100, 50))
                smallText1 = pygame.font.SysFont("comicsansms", 20)
                textSurf1, textRect1 = text_objects("Retry", smallText1)
                textRect1.center = ((150 + (100/2)), (450 + (50/2)))
                screen.blit(textSurf1, textRect1)

                if 250 > mouse1[0] > 150 and 500 > mouse1[1] > 450 and click1[0] == 1:
                    main()

                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                pygame.draw.rect(screen, red, (550, 450, 100, 50))
                smallText = pygame.font.SysFont("comicsansms", 20)
                textSurf, textRect = text_objects("Quit", smallText)
                textRect.center = ((550 + (100/2)), (450 + (50/2)))
                screen.blit(textSurf, textRect)

                if 650 > mouse[0] > 550 and 500 > mouse[1] > 450 and click[0] == 1:
                    quit_game()
                    
                pygame.display.update()

            
        #update screen      
        screen.fill(0)
        screen.blit(bg, (0,0))
        screen.blit(text, (570,0))
        
        for enemy in enemies:
            screen.blit(enemyImg, enemy)
            
        screen.blit(playerImg, startpos)
        score_count(score)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                gameExit = True
            
            #player movement
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    startpos[1] -= distance
                elif event.key == K_DOWN:
                    startpos[1] += distance
                elif event.key == K_LEFT:
                    startpos[0] -= distance
                elif event.key == K_RIGHT:
                    startpos[0] += distance

        pygame.display.update()
        frame_count += 1
        clock.tick(frame_rate)

if __name__ == '__main__':
    main()
    pygame.quit()
    quit()
