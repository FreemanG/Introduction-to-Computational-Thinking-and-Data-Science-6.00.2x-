# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab
#from ps3b_precompiled_27 import *  
''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        # TODO

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb
        # TODO

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb
        # TODO

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        self.getClearProb = random.random()
        if self.getClearProb < self.clearProb:
            return True
        else:
            return False
        # TODO

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        reproduceProb = random.random()
        if(reproduceProb < self.maxBirthProb * (1 - popDensity)):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException
        # TODO



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop
        # TODO

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses
        # TODO


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop
        # TODO


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.viruses)
        # TODO        


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        viruses_copy = self.viruses[:]
        pop_current = len(self.viruses)
        for i in range(pop_current):
            if(viruses_copy[i].doesClear()):
                self.viruses.remove(viruses_copy[i])
        
        pop_uncleared = len(self.viruses)
        self.popDensity = pop_uncleared/float(self.maxPop)
        
        viruses_copy2 = self.viruses[:]
        for j in range(pop_uncleared):
            try:            
                childVirus = viruses_copy2[j].reproduce(self.popDensity)
                self.viruses.append(childVirus)
            except NoChildException:
                pass
        
        pop_reproduced = len(self.viruses)
        return pop_reproduced
        # TODO



#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    pop=[]
    for i in range(300):
        pop.append(0)    
    # trials
    for n in range(numTrials):
        virusList = []
        for j in range(numViruses):
            virusList.append(SimpleVirus(maxBirthProb, clearProb))
        simPatient = Patient(virusList, maxPop)
    
        for k in range(300):
            pop[k] += simPatient.update()
    # calculate ave population
    avepop=[]
    for m in range(300):
        avepop.append(pop[m]/float(numTrials))
    
    # graphing
    pylab.plot(avepop)
    pylab.xlabel('Number of Time Steps')
    pylab.ylabel('Number of Virus Population')
    pylab.title('simulation Without Drug')
    pylab.legend()
    pylab.show()    
    
    # TODO

#simulationWithoutDrug(100, 1000, 0.1, 0.05, 10)

#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb
        # TODO


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances
        # TODO

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb
        # TODO

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        if (drug in self.resistances) and (self.resistances[drug] == True):
            return True
        else:
            return False
        # TODO


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        resistances_new = self.resistances
        for i in self.resistances:
            muteProb = random.random()
            if(muteProb < self.mutProb):
                resistances_new[i] = not resistances_new[i]

        count = 0
        for j in activeDrugs:
            if len(self.resistances)!=0 and self.resistances[j]:
                count += 1
            
        reproduceProb = random.random()
        if (count == len(activeDrugs)) and (reproduceProb < self.maxBirthProb * (1 - popDensity)):
            return ResistantVirus(self.maxBirthProb, self.clearProb, resistances_new, self.mutProb)
        else:
            raise NoChildException
        # TODO

            

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.postcondition = []
        Patient.__init__(self, self.viruses, maxPop)
        # TODO


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if(newDrug not in self.postcondition):
            self.postcondition.append(newDrug)
        # TODO


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.postcondition
        # TODO


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resisPop = 0
        for i in self.viruses: 
            count = 0
            resis = i.getResistances()
            for j in drugResist:
                if(j in resis) and (resis[j] == True):
                    count += 1
            if count == len(drugResist):
                resisPop += 1
        return resisPop
        # TODO


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        viruses_copy = self.viruses[:]
        pop_current = len(self.viruses)
        for i in range(pop_current):
            if(viruses_copy[i].doesClear()):
                self.viruses.remove(viruses_copy[i])
        
        pop_uncleared = len(self.viruses)
        popDensity = pop_uncleared/float(self.maxPop)
        
        viruses_copy2 = self.viruses[:]
        for j in range(pop_uncleared):
            try:       
                childVirus = viruses_copy2[j].reproduce(popDensity, self.postcondition)
                self.viruses.append(childVirus)
            except NoChildException:
                pass
        
        pop_reproduced = len(self.viruses)
        return pop_reproduced
        # TODO



#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    Pop = []
    resisPop = []
    for i in range(300):
        Pop.append(0)    
        resisPop.append(0)
    # trials
    for n in range(numTrials):
        virusList = []
        for j in range(numViruses):
            virusList.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        trePatient = TreatedPatient(virusList, maxPop)
    
        for k in range(150):
            Pop[k] += trePatient.update()
            resisPop[k] += trePatient.getResistPop(['guttagonol'])
        trePatient.addPrescription('guttagonol')
        for k in range(150, 300):
            Pop[k] += trePatient.update()
            resisPop[k] += trePatient.getResistPop(['guttagonol'])
            
    # calculate ave population
    avePop = []
    aveResisPop = []
    for m in range(300):
        avePop.append(Pop[m]/float(numTrials))
        aveResisPop.append(resisPop[m]/float(numTrials))
    
    # graphing
    pylab.plot(avePop, label = 'Average Total Pop')
    pylab.plot(aveResisPop, label = 'Average Guttagonol-Resistant Pop')
    pylab.xlabel('Number of Time Steps')
    pylab.ylabel('Number of Virus Population')
    pylab.title('simulation With Drug Additioned in the middle')
    pylab.legend(loc = 0)
    pylab.show()  
    # TODO

#simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 10)
#simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
#simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
#simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)