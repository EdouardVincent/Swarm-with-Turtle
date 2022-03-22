from turtle import*
import random
import time
from math import *

i=0

tortue1 = Turtle()
tortue2 = Turtle()
tortue3 = Turtle()
tortue4 = Turtle()

resultat_distance = 0

armée = [tortue1,tortue2,tortue3,tortue4]

tortue_couleur = ['red', 'yellow', 'green', 'pink']

def formule_distance (tortues_x, tortues_y) :
    return sqrt((tortues_y**2) + (tortues_x **2))


for x in range(len(armée)) : #assigner la couleur et lever stylo
    armée[x].color(tortue_couleur[x])
    armée[x].penup()
    

for x in range(len(armée)) : #mettre l'armée sur la meme ligne et augmenter la vitesse
    armée[x].speed(5000)
    armée[x].goto(0,i)

    i+=40
    
while True:
    
    for a in range(len(armée)) :
        tortue = armée[a]
        for b in range(len(armée)) :

            armée[b].speed(5000)
            armée[b].fd(10)
            
            tortues_y = (armée[b].pos()[1] - tortue.pos()[1])
            tortues_x = (tortue.pos()[0] - armée[b].pos()[0])
            
            
            resultat_distance = formule_distance(tortues_x, tortues_y)
        
        
            if resultat_distance < 50 and resultat_distance != 0 :
                armée[b].right(5)
                

            else :
                armée[b].left(5)

