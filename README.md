# mutual-exclusion-problem

A project I did for my CS bachelor in python.

## Quickstart

`python2 src/main.py`

# Introduction

Dans le cadre du cours de fonctionnement des ordinateurs, il fallait
créer un projet permettant de simuler deux processeurs voulant exécuter
une section critique. Le problème est que les deux processeurs ne
peuvent pas être en section critique en même temps, deux solutions sont
proposées pour essayer d'éviter ce cas, la solution simple et la
solution de Dekker, il a fallu simuler ces deux techniques. Pour
réaliser ce simulateur, il a fallu créer quatre grandes fonctions, les
deux premières permettant de simuler chacune des solutions, les deux
suivantes pour afficher le résultat

Le rapport ci-dessous décrit les solutions utilisées pour créer le
projet et les réponses aux questions demandées.

# Simulation des solutions

Le but du projet étant de simuler deux CPUs il a fallu trouver une
solution pour n'exécuter qu'une seule instruction à la fois, pour ce
faire, j'ai créé deux fonctions représentant chacune une méthode. Ces
fonctions reçoivent en paramètre l'instruction actuelle des CPU, b1 et
b2, exécutent l'instruction en revoyant la variable b1 modifiée ou non
et la prochaine instruction que le CPU devra exécuter. Pour simuler le
fait de n'exécuter qu'une seule instruction, il a fallu créer une
structure conditionnelle qui exécute des instructions en fonction de
l'instruction à exécuter transmise en paramètre.

## Solution simple

Voici comment fonctionne la fonction représentant la solution simple :

Elle reçoit en paramètre b1, b2 et l'instruction actuelle du CPU, elle
exécute ensuite l'instruction correspondante. À noter que b1 et b2 ne
représentent pas forcement véritablement b1 et b2, si c'est le CPU2 qui
appel la fonction b1 sera en fait b2 et l'inverse, si c'est le CPU1 les
bits ne sont modifiés.

Pour l'instruction 1, si b2 est différent de 1, on la prochaine
instruction sera la troisième sinon à la prochaine instruction sera la
deuxième. Pour ce faire on définit la variable instruction qui
représente la prochaine instruction à exécuter.

Pour l'instruction 2, on met la variable instruction à 1, c'est-à-dire
que tant que l'autre CPU est en dans sa section critique, on attend
qu'il ait fini.

Pour l'instruction 3, on met le b1 à 1 et on met la variable instruction
à 4.

Pour l'instruction 4, on passera simplement à l'instruction suivante,
car l'instruction représente la section critique où le CPU devrait
exécuter la section critique, mais le programme ne fait rien.

Pour l'instruction 5, on remet le b1 à 0, car le CPU a fini d'exécuter
sa section critique. Le CPU ayant fini d'exécuter sa section critique je
me suis dit qu'il était plus logique, dans le cas de cette simulation,
de redéfinir l'instruction suivante comme la première, en imaginant que
le CPU désire exécuter une nouvelle section critique.

Après avoir exécuté l'instruction, la fonction retourne b1 et le numéro
de la prochaine instruction qu'exécutera le CPU.

## Solution de Dekker

La fonction représentant la solution de Dekker est assez similaire à
celle de la solution de la solution simple, les instructions exécutées
et les paramètres sont différents.

La fonction reçoit b1, b2, tour, l'instruction du CPU et la variable
executeur qui représente le numéro du CPU qui veut exécuter une
instruction. Comme pour la solution simple, les b1 et b2 de la fonction
ne représentent pas forcément vraiment b1 et b2. La variable instruction
représente la même chose que dans la solution simple.

Pour l'instruction 1, on met la variable b1 et on passe à l'instruction
suivante au prochain appel de la fonction.

Pour l'instruction 2, si b2 est différent de 1, on exécutera
l'instruction 8 après celle-ci sinon, l'instruction suivante.

Pour l'instruction 3, on est dans le cas où b2 vaut 1, on met alors b1 à
0 et on passera à l'instruction suivante.

Pour l'instruction 4, c'est ici qu'il est important de savoir quel CPU
exécute une instruction, car on cherche on à savoir si c'est au tour du
CPU qui veut exécuter la section critique de le faire. La variable tour
vaut 1 ou 2, 1 signifie que c'est au tour du CPU 1 d'exécuter une
instruction s'il le désire sinon au CPU 2. On vérifie donc si c'est au
tour du CPU qui désire exécuter une instruction de le faire, si oui on
exécutera l'instruction 6, sinon l'instruction 5.

Pour l'instruction 5, on repasse à l'instruction 4 en mettant la
variable instruction à 4. On attend donc que ce soit au tour du CPU qui
désire exécuter une instruction de le faire pour passer à la suite des
instructions.

Pour l'instruction 6, on met b1 à 1 et on passera à l'instruction
suivante.

Pour l'instruction 7, on fera un saut à l'instruction 2 en mettant la
variable instruction à 2.

Pour l'instruction 8, on passe simplement à l'instruction suivante, car
l'instruction représente la section critique où le CPU devrait exécuter
la section critique, mais le programme ne fait rien.

Pour l'instruction 9, on veut donner le tour au CPU qui n'avait pas le
droit d'exécuter de section critique, pour ça on met la variable tour à
l'autre CPU, c'est-à-dire que si le CPU1 exécute cette instruction, tour
vaudra 2 sinon tour vaudra 1.

Pour l'instruction 10, on met b1 à 0 pour dire que le CPU n'est plus
dans sa section critique. On met la variable instruction à 1 pour les
mêmes raisons que dans la solution simple.

Après avoir exécuté l'instruction, la fonction retourne b1, la variable
tour et le numéro de la prochaine instruction qu'exécutera le CPU.

# 3 Affichage de l'état de la simulation

Il faut pouvoir afficher l'état actuel des instructions pour chaque CPU,
pour ce faire il a fallu créer deux fonctions, une qui affiche l'état
actuel des CPUs avec la solution simple et l'autre avec la solution de
Dekker.

Les deux fonctions fonctionnent de la même manière. Premièrement on crée
un tableau :

Exemple pour la solution simple

```
    Etape x -- b1 = y b2 = z
     * CPU 1 *                                    * CPU 2 *
     1: if b2 != 1 then goto 3                    1: if b1 != 1 then goto 3
     2: goto 1                                    2: goto 1
     3: b1 = 1                                    3: b2 = 1
     4: section critique                          4: section critique
     5: b1 = 0                                    5: b2 = 0
```

C'est la base de l'affichage, il faudra après remplacer x, y et z par
les valeurs correspondantes et déplacer des flèches à coter des
instructions qui représenteront quelles seront les prochaines
instructions exécutées.

Pour afficher le CPU2 et ses instructions correctement, on utilise
str.ljust() qui garantit qu'il y aura un certain nombre de caractères
entre la chaine de caractère et le coter gauche de la console.

Pour savoir où les flèches doivent être placées, on appelle la fonction
pointeur qui prend deux paramètres : l'instruction actuelle et
l'instruction à coter de laquelle on veut savoir s'il doit y avoir une
flèche. Si les deux paramètres sont égaux, on renvoie une chaine de
caractère représentant une flèche, sinon on renvoie une chaine de
caractère contenant un espace vide. On affiche à coter de chaque
instruction le résultat de la fonction.

Exemple à l'étape 0 pour la solution simple :

```
    Etape 0 -- b1 = 0 b2 = 0
     * CPU 1 *                                         * CPU 2 *
-->  1: if b2 != 1 then goto 3                    -->  1: if b1 != 1 then goto 3
     2: goto 1                                         2: goto 1
     3: b1 = 1                                         3: b2 = 1
     4: section critique                               4: section critique
     5: b1 = 0                                         5: b2 = 0
```

Après avoir créées toutes ces fonctions il faut les utiliser les
convenablement, c'est le rôle du main se trouvant dans projetfdo.py.

On commence par demander à l'utilisateur quelle solution il souhaite
utiliser, ensuite quelle simulation et enfin combien d'étapes il désire
simuler.

Après ça on met les variables b1 et b2 à 0, tour à 1. Instruction1 et
instruction2 représentent quelle sera l'instruction suivante que les
CPUs vont exécuter (instruction1 pour le CPU1 et instruction2 pour le
CPU2). La variable etapeActuelle représente l'étape actuelle de la
simulation. Ensuite on rentre dans une boucle qui s'exécute tant que
l'étape actuelle n'est pas l'étape de fin de la simulation.

Après ça on affiche le tableau de l'état actuel des CPUs et de leurs
instructions (exemple ci-dessus), puis si la simulation est automatique
on définit aléatoirement quel sera le prochain CPU à exécuter une
instruction, sinon on demande à l'utilisateur de choisir. Une fois
l'exécuteur définit, on appel la fonction correspondant à la solution
choisie au début, si l'exécuteur est le CPU2, on envoi le b1 de ka
fonction sera b2 et inversement, sinon les bits restent les même. La
fonction nous renvoie le b1 (ou b2 pour le CPU2) modifié ou non et la
prochaine instruction à exécuter pour le CPU. On vérifie alors que la
section critique n'est pas violée, pour ce faire on vérifie que
instruction1 et instruction2 ne valent pas 5 dans si la solution choisie
est la solution simple, sinon que instruction1 et instruction2 ne valent
pas 9. Dans le cas de la solution simple, on pourrait croire qu'il faut
vérifier si les instructions ne valent pas toutes les deux 4,
l'instruction qui représente la section critique, mais non, car ces
variables représentent la prochaine instruction à exécuter donc si ces
variables valent toutes les deux 5, ça veut dire qu'elles viennent
d'exécuter leur section critique, cette explication est la même pour la
solution de Dekker. Évidemment le cas où instruction1 et instruction2
valent 9 dans la solution de Dekker est impossible, car c'est justement
pour éviter une violation de la section critique que cette solution a
été inventée, mais on vérifie quand même.

Si jamais la section critique et violée on le signale et on continue le
simulateur pour voir ce qui se passe après, de plus les CPUs n'ont pas
de raisons de s'arrêter, car une violation de la section critique
n'engendre rien de telle sauf s'il y a une erreur, mais on suppose que
non.

Ensuite, si l'exécution est automatique, on fait une pause d'une
seconde. Après, on incrémente d'un l'étape actuelle et on refait un tour
de boucle si on n'est toujours pas arrivé à la dernière étape. En
sortant de la boucle, on affiche une dernière fois le tableau à la
dernière étape avant de finir la simulation.

# Questions*

1\. le bit i du processeur i représente la volonté d'exécuter sa section
critique, il vaut 1 quand il veut rentrer en section critique, sinon.
Lorsqu'il passe à l'étape 3, cela signifie que l'autre CPU est ou désire
déjà exécuter sa section critique, à partir de là deux cas sont
possibles.

---Soit le CPU1 est déjà dans sa section critique et alors le CPU2 doit
attendre son tour dans la boucle

```
4 if tour = 2 then goto 6 ;
5 goto 4 ;
```

Le CPU2 n'est pas en section critique et ne peux pas y entrer, son b2
est donc à 0. Lorsque le CPU1 aura fini d'exécuter sa section critique,
il mettra sa variable b1 à 0 et tour 2, le CPU2 pourra sortir de la
boucle et redemander un accès à la section critique.

--- Soit les deux processeurs ont voulu rentrer en même temps en section
critique
```
    Etape 0 -- b1 = 0 b2 = 0 tour = 1
     * CPU 1 *                         * CPU 2 *
-->  1: b1 = 1                    -->  1: b2 = 1
     2: if b2 != 1 goto 8              2: if b1 != 1 goto 8
```
Le processeur 1 exécute une instruction.
```
    Etape 1 -- b1 = 1 b2 = 0 tour = 1
     * CPU 1 *                         * CPU 2 *
     1: b1 = 1                    -->  1: b2 = 1
-->  2: if b2 != 1 goto 8              2: if b1 != 1 goto 8
```
Le processeur 2 exécute une instruction.
```
    Etape 2 -- b1 = 1 b2 = 1 tour = 1
     * CPU 1 *                         * CPU 2 *
     1: b1 = 1                         1: b2 = 1
-->  2: if b2 != 1 goto 8         -->  2: if b1 != 1 goto 8
```

Une fois dans ce cas, c'est la variable tour qui définira qui entre en
section critique. En effet , les deux CPU mettront leur bit à 0 et
tandis que l'un des processeurs restera bloqué dans une boucle en
attendant que la variable tour passe à son numéro, l'autre mettra son
bit à 1 et passera la condition 2 sans problème puisque l'autre
processeur n'a pas pu modifier son bit (à 0) car il est bloqué dans la
boucle.

2\. Imaginons d'abord que le CPU1 soit bloqué en section critique, ça
veut dire que b1 est à 1.

Dans le cas de la solution de Dekker, si le CPU2 veut rentrer dans la
section critique, il sera bloqué dans une boucle si tour vaut 1 il sera
bloqué dans la boucle 4, 5 en attendant son tour, si tour vaut 2, le
CPU2 sera bloquer dans la boucle suivante 2, 3, 4, 6, 7 en attendant que
le b1 passe à 0 ce qui n'arrivera jamais.

Boucle 2, 3, 4, 6, 7 :

```
* CPU 2 *
2: if b1 != 1 goto 8
3: b2 = 0
4: if tour = 2 goto 6
6: b2 = 1
7: goto 2
```

En utilisant la solution simple, le CPU2 restera bloqué en 1, 2 en
attendant que le b1 passe à 0, sauf si le CPU2 avait déjà exploité la
faille de cette solution, dans ce cas il effectuera une violation de la
section critique avant d'être bloqué dans la boucle 1, 2.

Boucle 1, 2 :

```
1: if b1 != 1 then goto 3
2: goto 1
```

Imaginons maintenant que le CPU1 soit bloqué dans le protocole
d\'entrée.

Si on utilise la solution de Dekker, plusieurs cas sont possible, si le
CPU1 est bloqué à l'instruction 1, 2, 6 ou 7, son b1 vaut alors 1, le
résultat est le même que si le CPU1 est bloqué en section critique (cf.
ci-dessus), s'il est bloqué à l'instruction 3, 4 ou 5, son b1 vaut alors
0 et le CPU2 peut exécuter tranquillement sa section critique.

En utilisant la solution simple, si le processeur 1 est bloqué à
l'instruction 1 ou 2 son b1 vaut alors 0 et le CPU2 peut exécuter
tranquillement sa section critique. Si le CPU1 est bloqué à
l'instruction 3 son b1 vaut 1, le CPU2 est bloqué dans la boucle 1, 2 en
attendant que b1 vaille 0 ce qui n'arrivera jamais.

# Conclusion

Ce projet permet donc de simuler et de comparer deux solutions
différentes d'accès concurrent à la mémoire grâce à quatre fonctions
principales, deux pour simuler les deux solutions et deux pour afficher
les résultats renvoyés par les fonctions.. On remarque effectivement que
la solution simple n'est pas envisageable à cause de la possibilité
qu'il y ait une violation de la section critique.

On remarque aussi que même en cas d'erreur avec la solution de Dekker où
un des deux processus resterait bloqué, la section critique ne sera
jamais violée.
