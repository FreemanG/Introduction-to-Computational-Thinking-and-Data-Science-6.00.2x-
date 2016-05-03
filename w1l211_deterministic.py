# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 20:00:31 2016

@author: Freeman
"""

import random

# Code Sapmple that is stochastic ????
mylist = []

for i in xrange(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print mylist

# Code Sample A deterministic
mylist = []

for i in xrange(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print mylist

    
# Code Sample B deterministic
mylist = []

random.seed(0)
for i in xrange(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
    print mylist