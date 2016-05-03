# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 17:08:28 2016

@author: Freeman
"""

import pylab
import random
import math

# Location
class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

# Field
class Field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

# Drunk
class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)] 
        return random.choice(stepChoices)
 
# walvVector       
def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())
    
    
# Simulation Result
loc = Location(0, 0)

d1 = UsualDrunk(Drunk('d1'))
d2 = ColdDrunk(Drunk('d2'))
d3 = EDrunk(Drunk('d3'))
d4 = PhotoDrunk(Drunk('d4'))
d5 = DDrunk(Drunk('d5'))
drunk = {d1:'UsualDrunk', d2:'ColdDrunk', d3:'EDrunk', d4:'PhotoDrunk', d5:'DDrunk'}

field = Field()
field.addDrunk(d1, loc)
field.addDrunk(d2, loc)
field.addDrunk(d3, loc)
field.addDrunk(d4, loc)
field.addDrunk(d5, loc)

numTrials = 1000
for d in drunk:
    X = [];
    Y = [];   
    for i in range(numTrials):
        X.append(0)
        Y.append(0)
        (X[i], Y[i]) = walkVector(field, d, random.randint(0, 1000))
    
    pylab.scatter(X, Y, label = drunk[d])
    pylab.legend(loc = 'best')
    pylab.xlim(-100, 100)
    pylab.ylim(-100, 100)
    pylab.figure()
