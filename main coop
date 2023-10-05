# Créé par GOLFINC, le 05/10/2023 en Python 3.7
import pygame, sys          # pour le jeu et la gestion de la fermeture
from random import *        # pour les rebonds aléatoires
from math import *          # pour le calcul d'angle avec sinus cosinus
from time import sleep      # pour le délai
import os





pygame.init()
pygame.font.init() # initalise une police pour l'affichage de texte
pygame.key.set_repeat(50)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 50)
fenetre = pygame.display.set_mode((1000, 650))
my_font = pygame.font.SysFont('Arial', 30)

done = False # condition de la game loop

score = 0
record = 43




class Balle:
    def __init__(self):
        self.pos = [fenetre.get_width() /2, fenetre.get_height() / 2]
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
        if self.pos[0] > fenetre.get_width() or self.pos[0] < 0:
            init()

        if self.pos[1] < 0 or self.pos[1] > fenetre.get_height():
            self.vect[1] = -self.vect[1]

    def collideCheck(self, raquette, direction):
        rect = pygame.Rect( raquette.pos[0], raquette.pos[1], raquette.dim[0], raquette.dim[1] )
        if rect.collidepoint(self.pos[0], self.pos[1]):
            self.rebondirRaquette(raquette, direction)

    def rebondirRaquette(self, raquette, direction):
        global score
        global record
        score += 1
        if score > record:
           record = score

        self.vitesse += 0.05

        if direction == "droite":
            self.a = random() * 2 - 1
        elif direction == "gauche":
            self.a = random() * 2 - 1 + pi

        self.vect = [cos(self.a), sin(self.a)]



class Raquette:
    def __init__(self, x):
        self.pos = [x, fenetre.get_height() / 2 - 60]
        self.dim = [10, 120]
        self.pas = 20

    def afficher(self):
        pygame.draw.rect(fenetre, [255, 255, 255], pygame.Rect(self.pos[0], self.pos[1], self.dim[0], self.dim[1]) )

    def suivre(self):
        self.pos[1] = pygame.mouse.get_pos()[1]
        if self.pos[1] + self.dim[1] > fenetre.get_height():
            self.pos[1] = fenetre.get_height() - self.dim[1]

    def haut(self):
        self.pos[1] -= self.pas

    def bas(self):
        self.pos[1] += self.pas


def init(record):
    global balle
    global raquettes

    sleep(2)

    balle = Balle()
    raquettes = [Raquette(50), Raquette(fenetre.get_width() - 60)]
    score = 0

init(0)

while done == False :

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN :
                raquettes[1].bas()

            if event.key == pygame.K_UP :
                raquettes[1].haut()


    fenetre.fill([50, 50, 70])

    text_surface = my_font.render('Score : ' + str(score) + " | Meilleur score : " + str(record), False, (255, 255, 255))
    fenetre.blit(text_surface, (20,20))

    raquettes[0].suivre()
    raquettes[0].afficher()
    raquettes[1].afficher()

    balle.collideCheck(raquettes[0], "droite")
    balle.collideCheck(raquettes[1], "gauche")
    balle.avancer()
    balle.afficher()

    pygame.display.flip()

pygame.quit()
