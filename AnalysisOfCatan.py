import random as r
import pandas as pd
import numpy as np



#Dice roll
def dieroll():
    die1 = r.randint(1, 6)
    die2 = r.randint(1, 6)
    rollVal = die1 + die2
    return rollVal

# function to run point count on player's current stats
def calcPoints(s,c,r,kc,vc):

    isLongestRoad = 0 if r < 5 else 1
    isLargestArmy = 0 if kc < 3 else 1
    points = s*1 + c*2 + 2*isLongestRoad + 2*isLargestArmy + vc
    return points

#initial starting out stats
settlements = 2
cities = 0
roads = 2
knightCards = 0
victoryCards = 0
currentTurn = 0

vPoints = calcPoints(settlements, cities, roads, knightCards, victoryCards)
map = pd.read_csv('ResourceMap.csv')
costMatrix = pd.read_csv('ItemCost.csv')


print (vPoints)





