# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:48:13 2016

@author: Freeman
"""
import random

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    choice=range(10, 21, 2)
    return random.choice(choice)