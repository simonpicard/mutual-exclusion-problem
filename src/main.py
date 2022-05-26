# -*- coding: utf-8 -*-

from random import randint
from time import sleep

from solutions import *

#importation de random pour générer un nombre aléatoire, sleep pour marquer une pause
#et du module solutions comprenant les fonctions nécéssaire au simulateur

solution = raw_input('Quelle solution voulez vous utilisez ? (1 - simple, 2 - Dekker)\n')
while solution != '1' and solution != '2':
    print 'Veuillez entrer soit "1", soit "2".'
    solution = raw_input('Quelle solution voulez vous utilisez ? (1 - simple, 2 - Dekker)\n')
#on demmande à l'utilisateur quelle solution il désire utiliser

if solution == '1':
    solution = 'solutionSimple'
else:
    solution = 'dekker'

simulation = raw_input('Simulation manuelle (1) ou automatique (2) ?\n')
while simulation != '1' and simulation != '2':
    print 'Veuillez entrer soit "1", soit "2".'
    simulation = raw_input('Simulation manuelle (1) ou automatique (2) ?\n')
#on demmande à l'utilisateur quelle simulation il désire utiliser

if simulation == '1':
    simulation = 'manuelle'
else:
    simulation = 'automatique'
    
etapeFin = raw_input('Nombre d’étapes ?\n')
while not etapeFin.isdigit():
    print 'Veuillez entrer un entier positif.'
    etapeFin = raw_input('Nombre d’étapes ?\n')
#on demmande à l'utilisateur combien d'étape il désire simuler

etapeFin = int(etapeFin)

print 'Début de la simultion\n'

b1 = 0
b2 = 0
tour = 1
etapeActuelle = 0

instruction1 = 1
instruction2 = 1
#les premières instructions que les CPUs exécuteront sont les premières
while etapeActuelle != etapeFin:
    #tant qu'on est pas arrivé à la dernière étape

    if solution == 'dekker':
        tableauDekker(etapeActuelle, b1, b2, tour, instruction1, instruction2)
    else:
        tableauSolutionSimple(etapeActuelle, b1, b2, instruction1, instruction2)
    print '\n',
    #on imprime le tableau en fonction de la solution choisie

    if simulation == 'automatique':
        #si la solution est automatique
        executeur = randint(1,2)
        #on choisi aléatoirement quel sera le prochain CPU à exécuter une instruction
    else:
        executeur = raw_input('Quel procésseur doit éxécuter une instruction ? (1 - CPU 1, 2 - CPU 2)\n')
        while executeur != '1' and executeur != '2':
            print 'Veuillez entrer soit "1", soit "2".'
            executeur = raw_input('Quel procésseur doit éxécuter une instruction ? (1 - CPU 1, 2 - CPU 2)\n')
        executeur = int(executeur)
        #sinon on demande à l'utilisateur de nous le dire

    print ''.ljust(3,' ')+' Le processeur '+str(executeur)+' exécute une instruction :'   
    print '\n',

    if executeur == 1:
        if solution == 'dekker':
            b1, tour, instruction1 = dekker(b1, b2, tour, instruction1, 1)
        else:
            b1, instruction1 = solutionSimple(b1, b2, instruction1)
    elif executeur == 2:
        if solution == 'dekker':
            b2, tour, instruction2 = dekker(b2, b1, tour, instruction2, 2)
        else:
            b2, instruction2 = solutionSimple(b2, b1, instruction2)
    #on simule une instruction d'un des processeurs choisi plus haut
    #en fonction de la solution choisie

    if (instruction1 == 9 and instruction2 == 9 and solution == 'dekker') or (instruction1 == 5 and instruction2 == 5 and solution == 'solutionSimple'):
        print '    Section critique violée !'
        print '    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯'
    #si la section critique est violée, c'est-à-dire que les deux CPUs y ont accès en même temps
    #on préviens l'utilisateur
    
    if simulation == 'automatique':
        sleep(1)
    #si la simulatione st automatique on marque une pause de une seconde

    etapeActuelle += 1
        
if solution == 'dekker':
    tableauDekker(etapeActuelle, b1, b2, tour, instruction1, instruction2)
else:
    tableauSolutionSimple(etapeActuelle, b1, b2, instruction1, instruction2)
#on affiche une dernière fois le tableau

print '\nFin de la simultion'
