import math
import random

## Fonction Plot
ndim = 2
NCELL = 2000
PCT_BEST = 35
## Découpage en 2 de la fonction pour simplifier 
ensemble_valeurs = [1,2,3,4,5,6]




##Boucle pour calculer la somme de x² et le cox(x)
## Le i pour le énième terme 

def fonction (ensemble_valeurs):
    a = 20
    b = 0.2
    c= 2*math.pi
    u = 0
    n = 0
    p = 0
    for i in range(len(ensemble_valeurs)):
        n += ensemble_valeurs[i]**2
        p += math.cos(c*ensemble_valeurs[i])

    u = -a*math.exp(-b*math.sqrt(1/len(ensemble_valeurs)*n))

    v = math.exp(1/len(ensemble_valeurs) * p) 

    fonction = u - v + a + math.exp(1)
    return fonction

#assert f < 1*10**-7
#print (fonction)

##Constante définit par papier f(x) = ax + b pour l'ensemble [-32,32]


def fct (x):
    e = 64
    r = -32
    resultat = e*x+r
    return resultat

min = fct(0)
max = fct(1)
best = fct(0.5)


class Cellule ():
    def __init__(self):
        self.genome = []
        
        for i in range(0, ndim):
            self.genome.append(random.random())
        self.reset()

    def apply (self):
        list_edit = []
        for i in range (len(self.genome)):
            list_edit.append(fct(self.genome[i]))
        self.output = fonction(list_edit)
    
    def reset (self):
        self.output = None

    def child (self): 
        child = Cellule()
        child.genome = self.genome.copy()
        n = random.randrange(0,len(child.genome))
        child.genome[n] = random.random()
        return child
        
    
def opti():
    # Initialisation
    cellules = []
    for _ in range(NCELL):
        cellules.append(Cellule())

    nbgeneration = 0
    while True:
        # Pour chaque génération:
        for cell in cellules:
            cell.apply()
        # On sélectionne les meilleures cellules
        trie = sorted(cellules, key = lambda inp: inp.output)
        print("GEN", nbgeneration, "SCORE", trie[0].output, "GENOME", trie[0].genome)
        # On calcule combien de cellules on garde (X% meilleures) Ncell = nombre cellule, pc best le top 20% ici
        ncut = NCELL * (PCT_BEST / 100)

        # On supprime toutes les autres cellules (pas dans les X% meilleures)
        cellules = trie[:int(ncut)]
        parent = 0
        while len(cellules) < NCELL:
            # On complète la génération par des enfants
            cellule_parent = cellules[parent]
            parent += 1    # L'index du parent qu'on sélectionne pour créer l'enfant, on incrément car on veut toujours prendre le meilleur, puis le second
            if parent >= ncut:
                parent = 0
            enfant = cellule_parent.child()    # On créé l'enfant
            cellules.append(enfant)    # On ajoute à la liste des cellules (pour la next gen)

        # Et z'est repartiiiiiiiiii
        nbgeneration += 1
        assert len(cellules) == NCELL


opti ()








   
