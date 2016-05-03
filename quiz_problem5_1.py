# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 19:30:54 2016

@author: Freeman
"""
import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
    count = 0.0
    
    for i in range(numTrials):
        ball1, ball2, ball3 = None, None, None
        bucket = [1, 1, 1, 1, 0, 0, 0, 0]        
        
        ball1 = random.choice(bucket)
        bucket.remove(ball1)
        ball2 = random.choice(bucket)
        bucket.remove(ball2)
        ball3 = random.choice(bucket)
        bucket.remove(ball3)
        
        if(ball1 == ball2 == ball3):
            count += 1
        
    return count/numTrials
            
        
        