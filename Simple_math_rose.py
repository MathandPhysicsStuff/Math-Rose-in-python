import pygame
from sys import exit
from math import cos, sin, pi
from time import sleep

from countingRationals11_9_2022 import smoothCount

pygame.init()
clock = pygame.time.Clock()

width = 760
height = 680
X = width//2
Y = height//2
drawFont = pygame.font.SysFont("serif",16)

darkBlue = (8, 8, 16)
BLUE = (0, 0, 255)
RED = (220, 0, 0)
lightGray = (200, 200, 200)

screen = pygame.display.set_mode((width, height))


def main():

    running = True
    
    i = 0
    draw = False

    r = smoothCount(25, 1)
    print(len(r))

    while running:
        
        screen.fill((darkBlue))
        draw_number(r[i])
        
        if draw == True:
         
            red = (13 + 11*i) % 256
            green = (29+ 17*i) % 256
            blue = (31 + 19*i) % 256
            drawColor = (red, green, blue)
            #print(drawColor)
        
            draw_rose(r[i], drawColor)
            sleep(0.5)
            #print(i)
            
            if i == len(r)-1:
                i = len(r)-1
            else:
                i += 1

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    draw = True

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    exit()


def draw_rose(r, color):

    t = 0
    a = 320
    step = pi/360
    k = r[0]/r[1]
    d = r[1]
    pygame.draw.rect(screen, BLUE, (0,0, width, height), 4) 
    while (t < 2*pi*d):

        r = a*cos(k*t)
        r2 = a*cos(k*(t+step))
        pygame.draw.circle(screen, color, (X + r*cos(t), Y + r*sin(t)), 1)

        #pygame.draw.line(screen, color, (X + r*cos(t), Y + r*sin(t)), (X + r2*cos(t+step), Y + r2*sin(t+step)), 2)
        t += step

def draw_number(r):

    k = r[0]/r[1]
    displayRect = pygame.Rect(0, 0, 180, 120)

    draw_n = drawFont.render("Numerator: " + str(round(r[0], 4)), 1, lightGray) 
    draw_d = drawFont.render("Denominator: " + str(round(r[1], 4)), 1, lightGray) 
    draw_k = drawFont.render("k = n/d: " + str(round(k, 4)), 1, lightGray) 

    screen.set_clip(displayRect)
    screen.fill(darkBlue)

    screen.blit(draw_n, (20, 20))
    screen.blit(draw_d, (20, 40))
    screen.blit(draw_k, (20, 60))

    screen.set_clip(None)

def countRationals(N):

    pass 



main()
