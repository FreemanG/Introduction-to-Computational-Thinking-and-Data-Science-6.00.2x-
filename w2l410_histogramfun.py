import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def Counts(word):
    counts=0
    length=float(len(word))
    for i in word:
        if(i in ['a', 'e', 'i', 'o', 'u']):
            counts+=1
    try:
        return counts/length
    except ZeroDivisionError:
        return float('NaN')
    
def Bin(numBins):
    #wordList=loadWords()
    BinPoints = []
    for j in wordList:
        BinPoints.append(Counts(j))
    mean = sum(BinPoints)/float(len(BinPoints))
    sd = stdDev(BinPoints)
    return (BinPoints, mean, sd)    

def labelPlot(numBins, mean, sd):
    pylab.title('the proportion of vowels in each word')
    pylab.xlabel('rates')
    pylab.ylabel('nums')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2,
               'Mean = ' + str(round(mean, 4))
               + '\nSD = ' + str(round(sd, 4)))  

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    val, mean, sd = Bin(numBins)
    pylab.hist(val, bins = numBins)
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    labelPlot(numBins, mean, sd)
    
    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
