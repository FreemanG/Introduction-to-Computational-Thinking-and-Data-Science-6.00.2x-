# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 21:35:49 2016

@author: Freeman
"""
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    yes = 0.0
    for i in range(numTrials):
        bucket = [1, 2, 3, 4, 5, 6]
        d1 = random.choice(bucket)
        bucket.remove(d1)
        d2 = random.choice(bucket)
        bucket.remove(d2)
        d3 = random.choice(bucket)
        bucket.remove(d3)
        if (d1%2==0 and d2%2==0 and d3%2==0) or (d1%2!=0 and d2%2!=0 and d3%2!=0):
            yes += 1
    return yes/numTrials
