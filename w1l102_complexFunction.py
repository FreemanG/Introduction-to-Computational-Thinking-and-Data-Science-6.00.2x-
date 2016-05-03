# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 21:03:59 2016

@author: Freeman
"""

def complexFunction(something, anotherThing, numberOfSillyWalks,
                    cansOfSpam, randomnessIndicator, isFurry,
                    frogsFound, isDoomsdayDeviceComplete):
    if(isDoomsdayDeviceComplete):
        print 'Doomsday device complete: Your cat requests a can of spam'
    else:
        print 'Doomsday device incomplete: Your cat stares at you'
    print str(something) + ' ' + str(anotherThing)
    print '# silly walks = ' + str(numberOfSillyWalks)
    print 'We have found ' + str(cansOfSpam) + ' cans of spam so far'
    if(randomnessIndicator):
        print 'Random! Oranges? I did not order an orange!'
    if(isFurry):
        fur = 'furry'
    else:
        fur = 'scary'
    print 'The ' + str(frogsFound) + ' frogs were very ' + fur

#complexFunction('cat', 'dragon', 100, 20, True, True, 1, False)


def simpleFunction(something, anotherThing, numberOfSillyWalks):
    cansOfSpam = 2 
    randomnessIndicator = True
    isFurry = False
    frogsFound = 1
    isDoomsdayDeviceComplete = False
    if(isDoomsdayDeviceComplete):
        print 'Doomsday device complete: Your cat requests a can of spam'
    else:
        print 'Doomsday device incomplete: Your cat stares at you'
    print str(something) + ' ' + str(anotherThing)
    print '# silly walks = ' + str(numberOfSillyWalks)
    print 'We have found ' + str(cansOfSpam) + ' cans of spam so far'
    if(randomnessIndicator):
        print 'Random! Oranges? I did not order an orange!'
    if(isFurry):
        fur = 'furry'
    else:
        fur = 'scary'
    print 'The ' + str(frogsFound) + ' frogs were very ' + fur

#simpleFunction('tea', 'dog', 10)


def complexWithDefaults(something, anotherThing, numberOfSillyWalks, 
                        cansOfSpam = 10, randomnessIndicator = True, 
                        isFurry = False, frogsFound = 1, isDoomsdayDeviceComplete = False):
    if(isDoomsdayDeviceComplete):
        print 'Doomsday device complete: Your cat requests a can of spam'
    else:
        print 'Doomsday device incomplete: Your cat stares at you'
    print str(something) + ' ' + str(anotherThing)
    print '# silly walks = ' + str(numberOfSillyWalks)
    print 'We have found ' + str(cansOfSpam) + ' cans of spam so far'
    if(randomnessIndicator):
        print 'Random! Oranges? I did not order an orange!'
    if(isFurry):
        fur = 'furry'
    else:
        fur = 'scary'
    print 'The ' + str(frogsFound) + ' frogs were very ' + fur

#complexWithDefaults('cat', 'werewolf', 1000)
#complexWithDefaults('cat', 'werewolf', 40, frogsFound = 80)