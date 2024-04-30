import pygame
import random

pygame.init()
pygame.font.init()

gameWidth=1200
gameHeight=900

white=(255,255,255)
black=(0,0,0)

gameDisplay=pygame.display.set_mode((gameWidth,gameHeight))
pygame.display.set_caption('Catch the rectangle')
fps=pygame.time.Clock()
    
def game_loop():
    gameExit = False
    bornapicture=pygame.image.load('borna.png')
    bornax_change=0
    bornay_change=0
    bornaWidth=30
    bornaHeight=30
    bornax=random.randrange(0,gameWidth)
    bornay=random.randrange(0,gameHeight)
    ballx=random.randrange(0,gameWidth)
    bally=random.randrange(0,gameHeight)
    ballWidth=25
    ballHeight=25
    ballx_change=5
    bally_change=5
    time=0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_END:
                    gameExit = True
                    pygame.quit()
                if event.key == pygame.K_w:
                    bornay_change = -5
                if event.key == pygame.K_s:
                    bornay_change = 5
                if event.key == pygame.K_a:
                    bornax_change = -5
                if event.key == pygame.K_d:
                    bornax_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_END:
                    quit()
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    bornay_change = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    bornax_change = 0    
        bornax += bornax_change
        bornay += bornay_change
        
        gameDisplay.fill(black)
        ball=pygame.draw.ellipse(gameDisplay, white, ((ballx,bally), (ballWidth,ballHeight)))
        borna=pygame.draw.rect(gameDisplay, False, ((bornax,bornay), (bornaWidth,bornaHeight)))
        gameDisplay.blit(bornapicture,(bornax,bornay))

        if ballx+50 > bornax:
            ballx_change=-5
        if bally+50 > bornay:
            bally_change=-5
        if ballx+50 > bornay:
            bally_change=5
        if bally+50 > bornax:
            ballx_change=5
        
        ballx += ballx_change
        bally += bally_change
        
        if bornax < -15:
            bornax = gameWidth+15
        if bornax > gameWidth+15:
            bornax = -15
        if bornay < -15:
            bornay = gameHeight+15
        if bornay > gameHeight+15:
            bornay = -15

        if ballx < -15:
            ballx = gameWidth+15
        if ballx > gameWidth+15:
            ballx = -15
        if bally < -15:
            bally = gameHeight+15
        if bally > gameHeight+15:
            bally = -15
        
        if borna.collidelist([ball]) > -1:
            gameExit=True
            if gameExit == True:
                time=pygame.time.get_ticks()
                time=time//1000
                bornax_change = 0
                bornay_change = 0
                ballx_change = 0
                bally_change = 0
                font=pygame.font.SysFont("Arial", 30)
                surface=font.render("Uspio si u {0} sekunde/i".format(time), False, white)
                gameDisplay.blit(surface,(gameWidth/2-50,gameHeight/2))
                pygame.font.SysFont.render
        pygame.display.update()
        fps.tick(120)
        
game_loop()
