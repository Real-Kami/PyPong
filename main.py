import pygame, sys
from pygame.locals import *
from random import *
from math import *

pygame.init()
pygame.font.init()

fenetre = pygame.display.set_mode((1000, 800))
my_font = pygame.font.SysFont('Arial', 30)

done = False

class Balle:
    def __init__(self):
        self.pos = [400, 400]
        self.vitesse = 1
        a = random() * 180
        self.vect = [cos(a), sin(a)]

    def afficher(self):
        posround = [ int(round(self.pos[0])), int(round(self.pos[1])) ]
        pygame.draw.circle(fenetre, [200, 200, 255], posround, 15)

    def avancer(self):
        self.pos[0] += self.vect[0] * self.vitesse
        self.pos[1] += self.vect[1] * self.vitesse

        if self.pos[0] > 1000:
            self.vect[0] = -self.vect[0]

        if self.pos[0] < 0:
            for i in range(len(raquettes)):
                print("score du joueur " + str(i) + " : " + str(raquettes[i].score))
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        if self.pos[1] < 0 or self.pos[1] > 800:
            self.vect[1] = -self.vect[1]

    def collideCheck(self, raquette):
        rect = pygame.Rect( raquette.pos[0], raquette.pos[1], 10, 120 )
        if rect.collidepoint(self.pos[0], self.pos[1]):

            raquette.score += 1

            barycentre = [raquette.pos[0] + raquette.dim[0] / 2,raquette.pos[1] + raquette.dim[1] / 2 ]
            centreSurface = [barycentre[0] + raquette.dim[0] / 2, barycentre[1]]

            x = centreSurface[0] - barycentre[0]
            y = centreSurface[1] - self.pos[1]

            angle = degrees(atan2(y, x))

            self.vect = [cos(angle), -sin(angle)]
            self.vect[0] = abs(self.vect[0])

            self.vitesse += 0.1

class Raquette:
    def __init__(self, x):
        self.pos = [x, 0]
        self.dim = [10, 120]
        self.score = 0

    def afficher(self):
        pygame.draw.rect(fenetre, [255, 255, 255], pygame.Rect(self.pos[0], self.pos[1], self.dim[0], self.dim[1]) )

    def suivre(self):
        self.pos[1] = pygame.mouse.get_pos()[1]

balle = Balle()
raquettes = [Raquette(50)]

while done == False :

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    fenetre.fill([50, 50, 70])
    fenetre.set_alpha(10)

    raquettes[0].suivre()
    raquettes[0].afficher()

    balle.collideCheck(raquettes[0])

    balle.avancer()
    balle.afficher()

    text_surface = my_font.render('Score : ' + str(raquettes[0].score), False, (255, 255, 255))
    fenetre.blit(text_surface, (20,20))

    pygame.display.flip()

pygame.quit()

#copyright Real-Kami 03/10/2023
