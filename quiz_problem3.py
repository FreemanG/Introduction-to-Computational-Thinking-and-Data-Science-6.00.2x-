# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 09:06:18 2016

@author: Freeman
"""

import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

pylab.plot(xVals, zVals, 'r', label = 'x z')
pylab.legend(loc = 'best')

pylab.plot(xVals, yVals, 'r', label = 'x y')
pylab.legend(loc = 'best')

pylab.plot(xVals, sorted(yVals), 'r', label = 'x sorted(y)')
pylab.legend(loc = 'best')

pylab.plot(sorted(xVals), yVals, 'r', label = 'sorted(x) y')
pylab.legend(loc = 'best')

pylab.plot(sorted(xVals), sorted(yVals), 'r', label = 'sorted(x) sorted(y)')
pylab.legend(loc = 'best')

pylab.hist(xVals)
pylab.hist(zVals)
pylab.hist(tVals)