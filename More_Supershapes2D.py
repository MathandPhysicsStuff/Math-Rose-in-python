import pygame
from sys import exit
from math import pi, cos, sin, pow

pygame.init()
clock = pygame.time.Clock()

width = 800
height = 680
X = width//2
Y = height//2

darkBlue = (8, 8, 16)
blue = (8, 8, 255)

screen = pygame.display.set_mode((width, height))

a = 1
b = 1    
n1 = 1
n2 = 1
n3 = 1
m = 5

def main():
    
    running = True
    while running:

        screen.fill(darkBlue)

        draw_supershapes(blue)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()
    exit()

def supershape(phi):

    t1 = cos(m*phi/4)
    t1 = abs(t1)
    t1 = pow(t1, n2)

    t2 = sin(m*phi/4)
    t2 = abs(t2)
    t2 = pow(t1 + t2, n3)

    r = pow(t2, 1/n1)

    if(abs(r) == 0):
        return 0

    else:
        return 1/r


def draw_supershapes(color):
    
    radius = 300 
    points = 2*pi/360

    for i in range(0, 361):

        phi0 = i * points
        phi1 = (i+1) * points

        r0 = supershape(phi0)
        r1 = supershape(phi1)

        x0 = X + (radius*r0*cos(phi0))
        y0 = Y + (radius*r0*sin(phi0))
        x1 = X + (radius*r1*cos(phi1))
        y1 = Y + (radius*r1*sin(phi1))

        pygame.draw.line(screen, color, (x0, y0), (x1, y1), 1)
        print(r0, r1)












main()
