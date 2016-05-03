import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO    
    for rabbit in range(CURRENTRABBITPOP):
        rabbitreproduceProb = random.random()
        if(rabbitreproduceProb < 1 - float(CURRENTRABBITPOP)/MAXRABBITPOP):
            if(CURRENTRABBITPOP < MAXRABBITPOP):
                CURRENTRABBITPOP += 1
                
         
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    for fox in range(CURRENTFOXPOP):
        eatrabbitProb = random.random()
        #succeeds in hunting
        if(eatrabbitProb < float(CURRENTRABBITPOP)/MAXRABBITPOP):
            if not(CURRENTRABBITPOP < 10 or CURRENTRABBITPOP == 10):
                CURRENTRABBITPOP -= 1
                foxreproduceProb = random.random()
                if(foxreproduceProb < 1.0/3):
                    CURRENTFOXPOP += 1
        #fails in hunting
        else:
            if not(CURRENTFOXPOP < 10 or CURRENTFOXPOP == 10):
                foxreproduceProb = random.random()
                if(foxreproduceProb < 1.0/10):
                    CURRENTFOXPOP -= 1
            
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations = [] 
    fox_populations = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    
    # graphing
    pylab.plot(rabbit_populations, label = 'rabbit_populations')
    pylab.plot(fox_populations, label = 'fox_populations')
    pylab.xlabel('Number of Time Steps')
    pylab.ylabel('Number of Population')
    pylab.title('simulate growth of fox and rabbit population in a forest!')
    pylab.legend(loc = 0)
    pylab.show()      
    
    return (rabbit_populations, fox_populations)


(rabbitPopulationOverTime, foxPopulationOverTime) = runSimulation(200)
coeff = pylab.polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff, range(len(rabbitPopulationOverTime))), label = 'rabbit')
coeff = pylab.polyfit(range(len(foxPopulationOverTime)), foxPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff, range(len(foxPopulationOverTime))), label = 'fox')
pylab.title(' evaluation the 2nd degree polynomial')
pylab.legend(loc = 0)
pylab.show()      
    