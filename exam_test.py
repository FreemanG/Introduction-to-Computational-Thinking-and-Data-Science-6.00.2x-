# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pylab

#problem 2-1
a = 1.0
b = 2.0
c = 4.0
yVals = []
xVals = range(-20, 20)
for x in xVals:
    yVals.append(a*x**2 + b*x + c)
yVals = 2*pylab.array(yVals)
xVals = pylab.array(xVals)
try:
    a, b, c, d = pylab.polyfit(xVals, yVals, 3)
    print a, b, c, d
except:
    print 'fell to here'
    
#problem 2-2
a1 = [0,1,2,3,4,5,6,7,8]   
a2 = [5,10,10,10,15] 
a3 = [0,1,2,4,6,8]
a4 = [6,7,11,12,13,15]
a5 = [9,0,0,3,3,3,6,6]
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5
    
#problem 2-3
def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)

