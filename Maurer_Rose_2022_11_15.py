import pygame
from sys import exit
from time import sleep
from math import pi, cos, sin
from random import randint
from countingRationals11_9_2022 import countRationals


pygame.init()
clock = pygame.time.Clock()

width = 720
height = 680
X = width // 2
Y = height // 2
drawFont = pygame.font.SysFont("serif",16)

#colors

black = (0, 0, 0)
white = (255, 255, 255)
darkBlue = (8, 8, 16)
Red = (255, 5, 5)
green = (0, 255, 0)
blue = (0, 0, 255)
lightGray = (220, 220, 220)

screen = pygame.display.set_mode((width, height))


def main():

    i = 0
    d = 1
    r = randint(1, 3) 
    N = countRationals(6, 1)
    running = True
    start = False

    while(running):

        screen.fill(darkBlue)
        
        if start == True:

            red = randint(10, 255)
            green = randint(10, 255)
            blue = randint(10, 255)
            color = (red, green, blue)
            
            displayNumbers(N[i], d)
            MaurerRose(N[i], d, color)
            #drawRose(N[i], color)

            if i < len(N)-1:
                i += 1
                sleep(0.5)
            else:
                i = len(N)-1
            
            """ 
            if d < 180:
                d += 15        
                sleep(0.2)

            else:
                d = 30
                sleep(0.4)
                if i < len(N)-1:
                    i += 1
                else:
                    i = len(N)-1    
            """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    start = True

                if event.key == pygame.K_a and i > 0:
                    i -= 1
                if event.key == pygame.K_d and i < len(N)-1:
                    i += 1
                if event.key == pygame.K_w:
                    d += 1

                if event.key == pygame.K_s:
                    d -= 1

                if event.key == pygame.K_z:
                    d -= 15 

                if event.key == pygame.K_x:
                    d += 15

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    exit()


def drawRose(N, color):
    
    a = 320
    t = 0
    n0 = N[0]
    n1 = N[1]
    n = n0/n1
    loop = (360*n1) + 1
    c = color
    
    for i in range(0, loop):

        k0 = (2*pi) * (i/361)
        k1 = (2*pi) * ((i+1)/361)
         
        r0 = a*sin(n*k0)
        r1 = a*sin(n*k1)

        x0 = X + r0*cos(k0)
        y0 = Y + r0*sin(k0)
        x1 = X + r1*cos(k1)
        y1 = Y + r1*sin(k1)

        pygame.draw.line(screen, c, (x0, y0), (x1, y1), 2)

        if N[0]/N[1] != 5/6:
            pygame.display.update()
            sleep(1/loop)

        if N[0]/N[1] == 5/6:
            c = Red

def MaurerRose(N, d, color):
    
    a = 320
    n = N[0]/N[1]
    loop = (360*N[1]) + 1 
    
    #pygame.draw.rect(screen, blue, (0, 0, width, height), 2)  
    for i in range(0, loop):
        

        k0 = (2*pi) * (i/361) * d
        k1 = (2*pi) * ((i+1)/361) * d 

        r0 = a*sin(n*k0)
        r1 = a*sin(n*k1)

        x0 = X + r0*cos(k0)
        y0 = Y + r0*sin(k0)
        x1 = X + r1*cos(k1)
        y1 = Y + r1*sin(k1)
        
        pygame.draw.line(screen, color, (x0, y0), (x1, y1), 1)
        
         
        if N[1] != 5/6: 
            pygame.display.update()
            sleep(1/loop)
        

def displayNumbers(N, d):
    
    n0 = N[0]
    n1 = N[1]
    n2 = N[0]/N[1]
    displayRect = pygame.Rect(0, 0, 180, 120)

    draw_n0 = drawFont.render("Numerator: " + str(n0), 1, lightGray)
    draw_n1 = drawFont.render("Denominator: " + str(n1), 1, lightGray)
    draw_n2 = drawFont.render("k =N/D: " + str(round(n2, 4)), 1, lightGray)
    draw_d = drawFont.render("degrees step: " + str(d), 1, lightGray)
    draw_loop = drawFont.render("loops: " + str(360*n1), 1, lightGray)
    
    screen.set_clip(displayRect)
    screen.fill(darkBlue)

    screen.blit(draw_n0, (10, 10))
    screen.blit(draw_n1, (10, 30))
    screen.blit(draw_n2, (10, 50))
    screen.blit(draw_d, (10, 70))
    screen.blit(draw_loop, (10, 90))

    screen.set_clip(None)


if __name__ == "__main__":
    main()













