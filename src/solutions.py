# -*- coding: utf-8 -*-

'''Module comprenant les fonction nécéssaire à la simulation de deux solutions différente pour un simulateur d’accès concurrent à la mémoire.'''

def solutionSimple(b1, b2, instruction):
    '''Cette fonction simule une instruction de la solution simple.'''
    if instruction == 1:
        #si on est à la 1e instruction
        instruction = 2
        if b2 != 1:
            instruction = 3
        #si b2 est différent de 1 on passe à l'instruction 3 sinon la 2e
    elif instruction == 2:
        #si on est à la 2e instruction
        instruction = 1
        #on repasse à l'instruction 1
    elif instruction == 3:
        #si on est à la 3e instruction
        b1 = 1
        instruction = 4
        #on met b1 à 1 et on passe à l'instruction suivante
    elif instruction == 4:
        #si on est à la 4e instruction
        instruction = 5
        #on est dans la section critique
        #on simule son exécution et on passe à l'instruction suivante
    elif instruction == 5:
        #si on est à la 5e instruction
        b1 = 0
        instruction = 1
        #on met b1 à 0 et on recommence les instructions
        #en imaginant que le CPU veut à nouveau exécuter une sectionc ritique
    return b1, instruction

def tableauSolutionSimple(etapeActuelle, b1, b2, instruction1, instruction2):
    '''Cette fonction affiche l'état actuelle des CPUs avec la solution simple.'''
    print '    Etape '+str(etapeActuelle)+' -- b1 = '+ str(b1) +' b2 = '+ str(b2)
    #on imprime les variables
    print '     * CPU 1 *'.ljust(40,' '),'* CPU 2 *'
    print pointeur(instruction1, 1),
    print '1: if b2 != 1 then goto 3'.ljust(30,' '),
    print pointeur(instruction2, 1),
    print '1: if b1 != 1 then goto 3'
    print pointeur(instruction1, 2),
    print '2: goto 1'.ljust(30,' '),
    print pointeur(instruction2, 2),
    print '2: goto 1'
    print pointeur(instruction1, 3),
    print '3: b1 = 1'.ljust(30,' '),
    print pointeur(instruction2, 3),
    print '3: b2 = 1'
    print pointeur(instruction1, 4),
    print '4: section critique'.ljust(30,' '),
    print pointeur(instruction2, 4),
    print '4: section critique'
    print pointeur(instruction1, 5),
    print '5: b1 = 0'.ljust(30,' '),
    print pointeur(instruction2, 5),
    print '5: b2 = 0'
    #on imprime toutes les instructions des deux CPUs
    #pour chaque instruction et chaque CPU
    #on vérifie si l'instruction affiché sera la prochaine exécutée
    #si c'est le cas on affiche '-->' sinon rien 
    

def dekker(b1, b2, tour, instruction, executeur):
    '''Cette fonction simule une instruction de la solution de Dekker.'''
    if instruction == 1:
        #si on est à la 1e instruction
        b1 = 1
        instruction = 2
        #on met b1 à 1 et on passe à l'instruction suivante
    elif instruction == 2:
        #si on est à la 2e instruction
        if b2 != 1:
            instruction = 8
        else:
            instruction = 3
        #si b2 est différent de 1 on passe à l'instruction 8 sinon à la suivante
    elif instruction == 3:
        #si on est à la 3e instruction
        b1 = 0
        instruction = 4
        #on met b1 à 0 et on passe à l'instruction suivante
    elif instruction == 4:
        #si on est à la 4e instruction
        if executeur == 1:
            #si le CPU qui exécute une instruction est le 1e
            if tour == 1:
                instruction = 6
            else:
                instruction = 5
        else:
            #si le CPU qui exécute une instruction est le 2e
            if tour == 2:
                instruction = 6
            else:
                instruction = 5
        #si la variable tour signifie que c'est au au tour du CPU qui veut exécuter une instruction de le faire
        #il passe à l'instruction 6 sinon à la suivante
    elif instruction == 5:
        #si on est à la 5e instruction
        instruction = 4
        #on repasse à l'instrution 4
    elif instruction == 6:
        #si on est à la 6e instruction
        b1 = 1
        instruction = 7
        #on met b1 à 1 et on passe à l'instruction suivante
    elif instruction == 7:
        #si on est à la 7e instruction
        instruction = 2
        #on repasse à l'instrution 2
    elif instruction == 8:
        #si on est à la 8e instruction
        instruction = 9
        #on est dans la section critique
        #on simule son exécution et on passe à l'instruction suivante
    elif instruction == 9:
        #si on est à la 9e instruction
        if executeur == 1:
            #si le CPU qui exécute une instruction est le 1e
            tour = 2
        else:
            #si le CPU qui exécute une instruction est le 2e
            tour = 1
        instruction = 10
        #on met donne le tour à l'autre CPU en modifiant la variable tour en fonction
        #et on passe à l'instruction suivante
    elif instruction == 10:
        #si on est à la 10e instruction
        b1 = 0
        instruction = 1
        #on met b1 à 0 et on recommence les instructions
        #en imaginant que le CPU veut à nouveau exécuter une sectionc ritique
    return b1, tour, instruction

def tableauDekker(etapeActuelle, b1, b2, tour, instruction1, instruction2):
    '''Cette fonction affiche l'état actuelle des CPUs avec la solution de Dekker.'''
    print '    Etape '+str(etapeActuelle)+' -- b1 = '+ str(b1) +' b2 = '+ str(b2) +' tour = '+ str(tour)
    #on imprime les variables
    print '     * CPU 1 *'.ljust(40,' '),'* CPU 2 *'
    print pointeur(instruction1, 1),
    print '1: b1 = 1'.ljust(30,' '),
    print pointeur(instruction2, 1),
    print '1: b2 = 1'
    print pointeur(instruction1, 2),
    print '2: if b2 != 1 goto 8'.ljust(30,' '),
    print pointeur(instruction2, 2),
    print '2: if b1 != 1 goto 8'
    print pointeur(instruction1, 3),
    print '3: b1 = 0'.ljust(30,' '),
    print pointeur(instruction2, 3),
    print '3: b2 = 0'
    print pointeur(instruction1, 4),
    print '4: if tour = 1 goto 6'.ljust(30,' '),
    print pointeur(instruction2, 4),
    print '4: if tour = 2 goto 6'
    print pointeur(instruction1, 5),
    print '5: goto 4'.ljust(30,' '),
    print pointeur(instruction2, 5),
    print '5: goto 4'
    print pointeur(instruction1, 6),
    print '6: b1 = 1'.ljust(30,' '),
    print pointeur(instruction2, 6),
    print '6: b2 = 1'
    print pointeur(instruction1, 7),
    print '7: goto 2'.ljust(30,' '),
    print pointeur(instruction2, 7),
    print '7: goto 2'
    print pointeur(instruction1, 8),
    print '8: section critique'.ljust(30,' '),
    print pointeur(instruction2, 8),
    print '8: section critique'
    print pointeur(instruction1, 9),
    print '9: tour = 2'.ljust(30,' '),
    print pointeur(instruction2, 9),
    print '9: tour = 1'
    print pointeur(instruction1, 10),
    print '10: b1 = 0'.ljust(30,' '),
    print pointeur(instruction2, 10),
    print '10: b2 = 0' 
    #on imprime toutes les instructions des deux CPUs
    #pour chaque instruction et chaque CPU
    #on vérifie si l'instruction affiché sera la prochaine exécutée
    #si c'est le cas on affiche '-->' sinon rien 

def pointeur(instructionActuelle, i):
    '''Renvoie une flèche si l'instruction i corresponds à l'instruction actuelle,
    une espace vide sinon'''
    res = '    '
    if instructionActuelle == i:
        res = '--> '
    #si l'instruction actuelle corresponds bien à celle qu'on s'aprête à afficher
    #on revoit une flèche, une espace vide sinon
    return res
