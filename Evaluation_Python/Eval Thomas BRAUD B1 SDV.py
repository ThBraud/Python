#!/usr/bin/env python3

import os
import time
import random
import platform

def random_boolean(prob):
    return random.random() <= prob

def to_string(game_of_life):
    s = "┌" + ("─" * (game_of_life.width * 2)) + "┐\n"
    for y in range(game_of_life.height):
        s += "│"
        for x in range(game_of_life.width):
            if game_of_life.grid[y][x]:
                s += "▓▓"
            else:
                s += "  "
        s += "│\n"
    s += "└" + ("─" * (game_of_life.width * 2)) + "┘\n"
    return s

def play(obj):
    is_windows = platform.system() == "Windows"
    print(to_string(obj))
    input("Press Enter to start")
    while True:
        if is_windows:
            os.system("cls")
        else:
            os.system("clear")

        print(to_string(obj))
        obj.update()
        time.sleep(0.05)
##Jeu de la vie                         ##Une fois sur deux le code ne marche pas, erreur venant de obj.update et du play(Game)
CelluleMorte = False
CelluleVivante = True
##Partie Principale 
class GameOfLife ():
    def __init__(self, height,width, prob_alive):
        self.width = width
        self.height = height
        self.prob_alive = prob_alive
        self.grid = []
    
        for line in range(height):
            line_data = list()
            for col in range(width):
                line_data.append(random_boolean(prob_alive))
                self.grid.append(line_data)
            if col < line:
                    col +=1
            else :
                    line +=1
        
    
        
    #Si la cellule rentre dans la grille elle est vivante sinon elle est morte 
    def is_alive (self, x, y):
     if (0 <= x < self.height) and (0 <= y < self.width):
        return CelluleVivante  
     else:
         return CelluleMorte
     
     ##Les coordonnes x et y sont bien dans la grille, l'etat de la cellule, change donc en cellule vivante
    def set_cell (self, x,y ):
        if (0 <= x < self.height) and (0 <= y < self.width):
            self.grid = [CelluleVivante]

    ##Nouvelle règles, j'aurai aime repartir de height, widht et ajouter la fonction Cellule;.
    def update (self,height,width):
        GameOfLife.set_cell()
        self.newgrid = []
        self.width = width
        self.height = height
        for line in range(height):
            line_data = []
            for col in range(width):
                self.newgrid.append(line_data)  
            if col < line:
                    col +=1
            else :
                    line +=1
        self.newgrid.append(line_data) 





        
    ##Cellules Voisines, Savoir si elle sont vivantes ou morte 
def Cellule (self,x,y):
        ##Cellule Gauche
        if (0 <= x-1 < self.height) and (0 <= y-1 < self.width):
            return CelluleVivante
        elif (0 > x-1 < self.height) and (0 > y-1 < self.width):
             return CelluleMorte
        
        ##Cellule Droite 
        elif (0 <= x+1 < self.height) and (0 > y+1 < self.width):
           return CelluleVivante
        elif (0 > x+1 < self.height) and (0 <= y-1 < self.width):
            return CelluleMorte
        
        ##Cellule Haute
        elif (0 <= x < self.height) and (0 <= y+1 < self.width):
            return CelluleVivante
        elif (0 > x < self.height) and (0 > y+1 < self.width):
            return CelluleMorte
        
        #Cellule Bas
        if (0 <= x < self.height) and (0 <= y-1 < self.width):
            return CelluleVivante
        elif (0 > x < self.height) and (0 <= y-1 > self.width):
            return CelluleMorte
        
        ##Cellule Diagonales Haute Gauche 
        elif (0 <= x-1 < self.height) and (0 <= y+1 < self.width):
            return CelluleVivante
        elif (0 > x-1 < self.height) and (0 > y+1 < self.width):
            return CelluleMorte
        
        ##Cellule Diagonales Basse Gauche
        elif (0 <= x-1 < self.height) and (0 <= y-1 < self.width):
            return CelluleVivante
        elif (0 > x-1 < self.height) and (0 > y-1 < self.width):
            return CelluleMorte
        
        ##Cellule Diagonales Haute Droite
        elif (0 <= x+1 < self.height) and (0 <= y+1 < self.width):
            return CelluleVivante
        elif (0 > x+1 < self.height) and (0 > y+1 < self.width):
            return CelluleMorte
        
        ##Cellule Diagonales Basse Droite
        elif (0 <= x+1 < self.height) and (0 <= y-1 < self.width):
            return CelluleVivante
        elif (0 > x+1 < self.height) and (0 > y-1 < self.width):
            return CelluleMorte


Game = GameOfLife(height=8, width=10, prob_alive=0.30)

play(Game)

