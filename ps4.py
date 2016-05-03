# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # parameters
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    conditions = [300, 150, 75, 0]
    
# trials
    for m in conditions:
        
        Pop = []
        Pop_eachTrial = []
        
        for n in range(numTrials):
            
            virusList = []
            for i in range(numViruses):
                virusList.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
            trePatient = TreatedPatient(virusList, maxPop)
    
            for j in range(m):
                Pop.append(trePatient.update())
            trePatient.addPrescription('guttagonol')    
            for j in range(m, m + 150):
                Pop.append(trePatient.update())
            
            Pop_eachTrial.append(Pop[-1])
            
        # graphing
        pylab.xlabel('Final Total Virus Population')
        pylab.ylabel('Number of Trials')
        pylab.title('The Effect of Delaying ' + str(m) + ' Times Treatment On Patinet Disease')
        pylab.hist(Pop_eachTrial, bins = 10)
        pylab.xlim(0, 200)
        pylab.figure()
# end of trials 
    


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
    # parameters
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    conditions = [300, 150, 75, 0]
    
# trials
    for m in conditions:
        
        Pop = []
        Pop_eachTrial = []
        
        for n in range(numTrials):
            
            virusList = []
            for i in range(numViruses):
                virusList.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
            trePatient = TreatedPatient(virusList, maxPop)
    
            for j in range(150):
                Pop.append(trePatient.update())
            trePatient.addPrescription('guttagonol')    
            for j in range(150, 150 + m):
                Pop.append(trePatient.update())
            trePatient.addPrescription('grimpex')
            for j in range(150 + m, 300 + m):
                Pop.append(trePatient.update())
            
            Pop_eachTrial.append(Pop[-1])
        
        mean = sum(Pop_eachTrial)/float(numTrials)
        sd = stdDev(Pop_eachTrial)
        # graphing
        pylab.xlabel('Final Total Virus Population')
        pylab.ylabel('Number of Trials')
        pylab.title('The Effect of Delaying ' + str(m) + ' Times Treatment On Patinet Disease')
        pylab.hist(Pop_eachTrial, bins = 20)
        pylab.xlim(0, 600)
        xmin, xmax = pylab.xlim()
        ymin, ymax = pylab.ylim()
        pylab.text((xmax-xmin)*0.8, (ymax-ymin)/2,
               'Mean = ' + str(round(mean, 4)) + '\nSD = ' + str(round(sd, 4)))
        pylab.figure()
        

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5