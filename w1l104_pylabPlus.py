# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 21:32:00 2016

@author: Freeman
"""

'''
default x axis
'''
import pylab
pylab.figure(1) #make figure 1 current figure
pylab.plot([1,2,3,4], [1,2,3,4])
pylab.figure(2)
pylab.plot([1,4,2,3], [5,6,7,8])
pylab.savefig('figure-eric') #save figure 2
pylab.figure(1)
pylab.plot([5,6,10,3]) 
#x-values will default, to range of whatever the length of the y-values is
#x-values will be 0,1,2,3
pylab.savefig('figure-grimson')
#pylab.show()

'''
title
'''
principal = 10000 #initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(range(years + 1), values)
pylab.title('5% growth, compounded annually') #title
pylab.xlabel('years of compunding') #xlabel
pylab.ylabel('value of principal $') #ylabel
pylab.show()

'''
format
'''
principal = 10000 #initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(range(years + 1), values, 'ro')
pylab.title('5% growth, compounded annually') #title
pylab.xlabel('years of compunding') #xlabel
pylab.ylabel('value of principal $') #ylabel
pylab.show()

'''
format2
'''
principal = 10000 #initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(values, linewidth =30) #default x
pylab.title('5% growth, compounded annually', fontsize = 12) #title
pylab.xlabel('years of compunding', fontsize = 6) #xlabel
pylab.ylabel('value of principal $', fontsize = 20) #ylabel
pylab.show()