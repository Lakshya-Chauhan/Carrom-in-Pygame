import pygame
from variables import *
from os import system
FoNt = 0
FoNtprint = 0
strikerClicked = False
def cls():
    system("cls")
def font(a:str,b=18):
    global FoNt
    FoNt = pygame.font.SysFont(a,b)
def printpy(x:str,a=(100,400),y=(128,128,128)):
    global FoNt,FoNtprint
    FoNtprint = FoNt.render(x,True,y)
    screen.blit(FoNtprint,a)
if __name__ == "__main__":
    frameRate = 200
    dt = 1/200

    pygame.init()
    screen = pygame.display.set_mode((800,800))
    #icon = pygame.image.load('')
    pygame.display.set_caption("Carrom")
    #pygame.display.set_icon(icon)
    board = pygame.image.load("assets/images/board.png")
    arrow = pygame.image.load("assets/images/arrowt.png")
    cls()
    running = True
    clock = pygame.time.Clock()
    while running == True:
        initTime = time.time()
        clock.tick(frameRate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    mpos = pygame.mouse.get_pos()
                    if distance(mpos, coins[-1].pos) < coins[-1].radius:
                        strikerClicked = True
        
        #Code Here
        screen.blit(board,(0,0))
        collisions.clear()
        for i in coins:
            collisions.extend(i.collision([objs for objs in coins if objs.number != i.number], collisions, dt))
            i.update(dt)
            i.display(screen)
        if strikerClicked == True:
            if pygame.mouse.get_pressed()[0] == True:
                mpos = pygame.mouse.get_pos()
                distBetween = distance(mpos, coins[-1].pos)
                angleVector = pygame.Vector2(-(coins[-1].pos[0] - mpos[0]), -(coins[-1].pos[1] - mpos[1]))
                Yaxis = pygame.Vector2(0,1)
                if distBetween < 120:
                    tempImg = pygame.transform.rotate(pygame.transform.scale(arrow, (20, 2*distBetween)), angleVector.angle_to(Yaxis))
                    screen.blit(tempImg, ((coins[-1].pos[0] - tempImg.get_width()/2), (coins[-1].pos[1] - tempImg.get_height()/2)))
                    pygame.draw.circle(screen, (20, 200, 50), coins[-1].pos, distBetween, 1)
                    coins[-1].display(screen)
                else:
                    tempImg = pygame.transform.rotate(pygame.transform.scale(arrow, (20, 240)), angleVector.angle_to(Yaxis))
                    screen.blit(tempImg, ((coins[-1].pos[0] - tempImg.get_width()/2), (coins[-1].pos[1] - tempImg.get_height()/2)))
                    pygame.draw.circle(screen, (20, 200, 50), coins[-1].pos, 120, 1)
                    coins[-1].display(screen)

            else:
                strikerClicked = False
                mpos = pygame.mouse.get_pos()
                angleVector = pygame.Vector2((coins[-1].pos[0] - mpos[0]), (coins[-1].pos[1] - mpos[1]))
                if angleVector.magnitude() < 30:
                    coins[-1].vel += angleVector*5
                else:
                    coins[-1].vel += angleVector*10
                coins[-1].x = coins[-1].vel[0]
                coins[-1].y = coins[-1].vel[1]

        pygame.display.update()
        endTime = time.time()
        dt = endTime-initTime
        if dt != 0: frameRate = 1/dt
        else: frameRate = 3400
