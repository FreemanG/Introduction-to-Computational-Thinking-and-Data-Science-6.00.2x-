# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 21:23:55 2016

@author: Freeman
"""

def isAlphabeticalWord(word, wordList=None):
    if (len(word) > 0):
        curr = word[0]
    for letter in word:
        if (curr > letter):
            return False
        else:
            curr = letter
    if wordList is None:
        return True
    return word in wordList
    
'''
For example, isAlphabeticalWord('abcd') should return True 
but isAlphabeticalWord('zoo') should return False.
'''