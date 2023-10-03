import pygame, sys          # pour le jeu et la gestion de la fermeture
from random import *        # pour les rebonds aléatoires
from math import *          # pour le calcul d'angle avec sinus cosinus
from time import sleep      # pour le délai
import os





pygame.init()
pygame.font.init() # initalise une police pour l'affichage de texte

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 50)
fenetre = pygame.display.set_mode((1000, 650))
my_font = pygame.font.SysFont('Arial', 30)

done = False # condition de la game loop





class Balle:
    def __init__(self):
        self.pos = [fenetre.get_width() - 50, fenetre.get_height() / 2]
        self.vitesse = 1
        self.a = 0
        self.vect = [cos(self.a), sin(self.a)]

    def afficher(self):
        posround = [ int(round(self.pos[0])), int(round(self.pos[1])) ]
        pygame.draw.circle(fenetre, [200, 200, 255], posround, 15)

    def avancer(self):
        self.pos[0] += self.vect[0] * self.vitesse
        self.pos[1] += self.vect[1] * self.vitesse
        self.rebondir()

    def rebondir(self):
        if self.pos[0] > fenetre.get_width():
            self.vect[0] = -self.vect[0]

        if self.pos[1] < 0 or self.pos[1] > fenetre.get_height():
            self.vect[1] = -self.vect[1]

        self.gameover()

    def gameover(self):
        if self.pos[0] < 0:
            sleep(3)
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    def collideCheck(self, raquette):
        rect = pygame.Rect( raquette.pos[0], raquette.pos[1], 10, 120 )
        if rect.collidepoint(self.pos[0], self.pos[1]):
            self.rebondirRaquette(raquette)

    def rebondirRaquette(self, raquette):
        raquette.score += 1
        self.vitesse += 0.1
        self.a = random() * 2 - 1
        self.vect = [cos(self.a), sin(self.a)]



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



sleep(1)

while done == False :

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    fenetre.fill([50, 50, 70])

    text_surface = my_font.render('Score : ' + str(raquettes[0].score), False, (255, 255, 255))
    fenetre.blit(text_surface, (20,20))

    raquettes[0].suivre()
    raquettes[0].afficher()

    balle.collideCheck(raquettes[0])
    balle.avancer()
    balle.afficher()

    pygame.display.flip()

pygame.quit()
