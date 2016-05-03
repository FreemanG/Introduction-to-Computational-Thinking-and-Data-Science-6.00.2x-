# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 22:11:08 2016

@author: Freeman
"""

def stdDevOfLengths(L):
    sum=0
    tot = 0.0
    for i in L:
        sum+=len(i)
    try: 
        mean = sum/float(len(L))
        for j in L:
            tot += (len(j) - mean)**2
        return (tot/len(L))**0.5
    except ZeroDivisionError:
        return(float('NaN'))
    
'''   

    Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.

    Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'], stdDevOfLengths(L) should return 1.8708.

'''