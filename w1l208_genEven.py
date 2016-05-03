# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # Your code here
    choice = range(0, 100, 2)
    return random.choice(choice)