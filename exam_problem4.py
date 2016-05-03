import pylab
import random



class Location(object):
    
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        self.leftEdge = -50
        self.rightEdge = 50
        self.bottomEdge = -50
        self.topEdge = 50
        
    def move(self, deltaX, deltaY, fence):
        """deltaX and deltaY are floats"""
        
        if fence == 'SW':
            if self.x + deltaX > self.leftEdge and self.x + deltaX < self.rightEdge:
                self.x += deltaX
            if self.y + deltaY > self.bottomEdge and self.y + deltaY < self.topEdge:
                self.y += deltaY
        
        elif fence == 'SP':
            if self.x + deltaX > self.leftEdge  and self.x + deltaX < self.rightEdge:
                self.x += deltaX
            elif self.x + deltaX > self.rightEdge:
                self.x = self.leftEdge + (self.x + deltaX - self.rightEdge)
            elif self.x + deltaX < self.leftEdge:
                self.x = self.rightEdge - (self.leftEdge - (self.x + deltaX))

            if self.y + deltaY > self.bottomEdge and self.y + deltaY < self.topEdge:
                self.y += deltaY
            elif self.y + deltaY > self.topEdge:
                self.y = self.bottomEdge + (self.y + deltaY - self.topEdge)
            elif self.y + deltaY < self.bottomEdge:
                self.y = self.topEdge - (self.bottomEdge - (self.y + deltaY))
            
        elif fence == 'WW':
            if self.x + deltaX < self.rightEdge and self.x + deltaX > self.leftEdge:
                self.x += deltaX
            elif self.x + deltaX > self.rightEdge:
                self.x = self.topEdge
            elif self.x + deltaX < self.leftEdge: 
                self.x = self.bottomEdge
                
            if self.y + deltaY < self.topEdge and self.y + deltaY > self.bottomEdge:
                self.y += deltaY
            elif self.y + deltaY > self.topEdge: 
                self.y = self.rightEdge
            elif self.y + deltaY < self.bottomEdge:  
                self.y = self.leftEdge
            
        elif fence == 'BH':          
            if self.x + deltaX < self.rightEdge and self.x + deltaX > self.leftEdge and self.y + deltaY < self.topEdge and self.y + deltaY > self.bottomEdge:
                self.x += deltaX
                self.y += deltaY
            else:
                self.x = self.leftEdge + (self.rightEdge - self.leftEdge)/2
                self.y = self.bottomEdge + (self.topEdge - self.bottomEdge)/2
               
        return Location(self.x, self.y)
    
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



class Field(object):
    
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk, fence):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist, fence)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]



class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name
 

 
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(-1.0,-1.0),(-1.0,0.0),(-1.0,1.0),(0.0,1.0),(0.0,-1.0),(1.0,-1.0),(1.0,0.0),(1.0,1.0)]
        return random.choice(stepChoices)
 


# walkVector       
# f-field, d-drunk, fc-fence
#def walkVector(f, d, numSteps, fc):
#    start = f.getLoc(d)
#    for s in range(numSteps):
#        f.moveDrunk(d, fc)
#    return(f.getLoc(d).getX() - start.getX(),
#           f.getLoc(d).getY() - start.getY())
def walkVector(f, d, numSteps, fc):
    for s in range(numSteps):
        f.moveDrunk(d, fc)
    return(f.getLoc(d).getX(), f.getLoc(d).getY())
    
    
# Simulation Result
loc = Location(0, 0)

d1 = UsualDrunk(Drunk('d1'))
d2 = UsualDrunk(Drunk('d2'))
d3 = UsualDrunk(Drunk('d3'))
d4 = UsualDrunk(Drunk('d4'))
drunk = {d1:'SW', d2:'SP', d3:'WW', d4:'BH'}

field = Field()
field.addDrunk(d1, loc)
field.addDrunk(d2, loc)
field.addDrunk(d3, loc)
field.addDrunk(d4, loc)

numTrials = 500
for d in drunk:
    X = [];
    Y = [];   
    for i in range(numTrials):
        X.append(0)
        Y.append(0)
        (X[i], Y[i]) = walkVector(field, d, random.randint(0, 100), drunk[d])
    
    pylab.scatter(X, Y, label = drunk[d], s = 10)
    pylab.legend(loc = 'best')
    pylab.xlim(-60, 60)
    pylab.ylim(-60, 60)
    pylab.figure()

