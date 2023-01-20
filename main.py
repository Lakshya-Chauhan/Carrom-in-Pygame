import pygame
from variables import *
from os import system
FoNt = 0
FoNtprint = 0
strikerClicked = False
players = 2
turn = 0
sliderPos = [400, 400]
sliderClicked = False
moving = False
def cls():
    system("cls")


def font(a: str, b=18):
    global FoNt
    FoNt = pygame.font.SysFont(a, b)


def printpy(x: str, a=(100, 400), y=(128, 128, 128)):
    global FoNt, FoNtprint
    FoNtprint = FoNt.render(x, True, y)
    screen.blit(FoNtprint, a)


if __name__ == "__main__":
    frameRate = 1000
    dt = 1/1000

    pygame.init()
    screen = pygame.display.set_mode((800, 1000))
    icon = pygame.image.load('assets/images/icon.jpg')
    pygame.display.set_caption("Carrom")
    pygame.display.set_icon(icon)
    board = pygame.image.load("assets/images/board.png")
    arrow = pygame.image.load("assets/images/arrowt.png")
    slider = pygame.image.load("assets/images/slidert.png")
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
                        if moving == False:
                            strikerClicked = True

        # Code Here
        screen.fill((200, 200, 200))
        screen.blit(board, (0, 100))
        if players == 2:
            if turn%2 == 0:
                temp_slider = pygame.transform.scale(slider,(slider.get_width(), slider.get_height()))
                if moving == True:
                    temp_slider.set_alpha(100)
                screen.blit(temp_slider, (158, 32.5))
                temp_slider = pygame.transform.scale(slider,(slider.get_width(), slider.get_height()))
                temp_slider.set_alpha(100)
                screen.blit(temp_slider, (158, 932.5))
            else:                
                temp_slider = pygame.transform.scale(slider,(slider.get_width(), slider.get_height()))
                if moving == True:
                    temp_slider.set_alpha(100)
                screen.blit(temp_slider, (158, 932.5))
                temp_slider = pygame.transform.scale(slider,(slider.get_width(), slider.get_height()))
                temp_slider.set_alpha(100)
                screen.blit(temp_slider, (158, 32.5))
        collisions.clear()
        for i in coins:
            collisions.extend(i.collision(
                [objs for objs in coins if objs.number != i.number], collisions, dt))
            if moving == True:
                i.update(dt)
            i.display(screen)
        if moving == False:
            if turn%2 == 1:
                if pygame.mouse.get_pressed()[0] == True:
                    mpos = pygame.mouse.get_pos()
                    if distance(mpos, [sliderPos[1],950]) < 17.5 or sliderClicked == True:
                        sliderClicked = True
                        if mpos[0] >= 158+coins[-1].radius and mpos[0] <= 641-coins[-1].radius:
                            if len([1 for i in coins[:-1] if distance(i.pos, (mpos[0], coins[-1].pos[1])) < coins[-1].radius+i.radius]) == 0:
                                sliderPos[1] = mpos[0]
                        coins[-1].pos[0] = sliderPos[1]
                else:
                    sliderClicked = False
                pygame.draw.circle(screen, (65, 125, 212), (sliderPos[1], 950), 17.5)
            if turn%2 == 0:
                if pygame.mouse.get_pressed()[0] == True:
                    mpos = pygame.mouse.get_pos()
                    if distance(mpos, [sliderPos[0],50]) < 17.5 or sliderClicked == True:
                        sliderClicked = True
                        if mpos[0] >= 158+coins[-1].radius and mpos[0] <= 641-coins[-1].radius:
                            if len([1 for i in coins[:-1] if distance(i.pos, (mpos[0], coins[-1].pos[1])) < coins[-1].radius+i.radius]) == 0:
                                sliderPos[0] = mpos[0]
                        coins[-1].pos[0] = sliderPos[0]
                else:
                    sliderClicked = False
                pygame.draw.circle(screen, (65, 125, 212), (sliderPos[0], 50), 17.5)
        else:
            if stopped(coins) == len(coins):
                sliderPos = [400, 400]
                if turn%2 == 0:
                    for j in range(158+23,641-23):
                        if len([1 for i in coins[:-1] if distance(i.pos, (j, coins[-1].pos[1])) < coins[-1].radius+i.radius]) == 0:
                            sliderPos[0] = j
                    coins[-1].pos = [sliderPos[0], 142+100]
                else:
                    for j in range(158+23,641-23):
                        if len([1 for i in coins[:-1] if distance(i.pos, (j, coins[-1].pos[1])) < coins[-1].radius+i.radius]) == 0:
                            sliderPos[1] = j
                    coins[-1].pos = [sliderPos[1], 657+100]
                moving = False
                        


        if strikerClicked == True:
            if pygame.mouse.get_pressed()[0] == True:
                mpos = pygame.mouse.get_pos()
                distBetween = distance(mpos, coins[-1].pos)
                if distBetween > 23.69:
                    angleVector = pygame.Vector2(
                        -(coins[-1].pos[0] - mpos[0]), -(coins[-1].pos[1] - mpos[1]))
                    Yaxis = pygame.Vector2(0, 1)
                    if distBetween < 120:
                        tempImg = pygame.transform.rotate(pygame.transform.scale(
                            arrow, (20, 2*distBetween)), angleVector.angle_to(Yaxis))
                        screen.blit(tempImg, ((
                            coins[-1].pos[0] - tempImg.get_width()/2), (coins[-1].pos[1] - tempImg.get_height()/2)))
                        pygame.draw.circle(screen, (20, 200, 50),
                                           coins[-1].pos, distBetween, 2)
                        coins[-1].display(screen)
                    else:
                        tempImg = pygame.transform.rotate(pygame.transform.scale(
                            arrow, (20, 240)), angleVector.angle_to(Yaxis))
                        screen.blit(tempImg, ((
                            coins[-1].pos[0] - tempImg.get_width()/2), (coins[-1].pos[1] - tempImg.get_height()/2)))
                        pygame.draw.circle(screen, (20, 200, 50),
                                           coins[-1].pos, 120, 2)
                        coins[-1].display(screen)

            else:
                strikerClicked = False
                mpos = pygame.mouse.get_pos()
                angleVector = pygame.Vector2(max(distance(coins[-1].pos, mpos)-23.69, 0.01))
                angleVector = angleVector.rotate(angleVector.angle_to(pygame.Vector2((coins[-1].pos[0] - mpos[0]), (coins[-1].pos[1] - mpos[1]))))
                if angleVector.magnitude() > 1:
                    coins[-1].vel += angleVector*20
                    coins[-1].x = coins[-1].vel[0]
                    coins[-1].y = coins[-1].vel[1]
                    moving = True
                    turn+=1

        pygame.display.update()
        endTime = time.time()
        dt = endTime-initTime
        if dt != 0:
            frameRate = 1/dt
        else:
            frameRate = 3400
