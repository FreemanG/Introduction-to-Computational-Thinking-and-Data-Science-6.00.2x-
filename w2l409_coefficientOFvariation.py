# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5
    
def CV(X):
    mean=sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('NaN')

X=[10, 4, 12, 15, 20, 5]       