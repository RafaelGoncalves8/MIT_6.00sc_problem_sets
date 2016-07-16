## Probability and Randomness
# non-determinism
# Stochastic processes - next state depends on previous state + random element
# random.random => float between 0.0 and 1.0

import random

def rollDie():
    """ Returns value between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

def testRoll(n = 10):
    result = " "
    for i in range(n):
        result = result + str(rollDie())
        print (result)

## PyLab
import pylab


#pylab.figure(1)
#pylab.plot([1,2,3,4],[1,2,3,4])
#pylab.figure(2)
#pylab.plot([1,4,2,3],[5,6,7,8])
#pylab.savefig("firstsave")
#pylab.figure(1)
#pylab.plot([5,6,7,10])
#pylab.savefig("secondsave")
#pylab.show()

#principal = 10000
#interestRate = 0.05
#years = 20
#values = []
#for i in range(years+1):
#    values.append(principal)
#    principal += principal*interestRate
#pylab.plot(values)
#
#pylab.title( "5% Growth - Compounded Annually")
#pylab.xlabel( "Years of Compounfing")
#pylab.ylabel( "Value of Principal ($)")
#
#pylab.show()

def checkPascal (numTrials):
    yes = 0.0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 ==6:
                yes += 1
                break
    print "Probability of losing = " +str(1.0 - yes/numTrials)

#checkPascal(1000)

## Monte Carlo simulation
# Inferential statistics
#  - random sample tends to exhibit the same properties as population of sample
 
def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads/numFlips

##def flipSim(numFlipsPerTrial, numTrials):
##    fracHeads = []
##    for i in range(numTrials):
##        fracHeads.append(flip(numFlipsPerTrial))
##    mean = sum(fracHeads)/float(len(fracHeads))
##    return (mean)

# Law of Large Numbers
# - repeted independent tests with the same actual probability, p, the chance that the fraction of times outcome occurs converges to p as trials tends to infinity

def flipPlot(minExp, maxExp):
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
    #pylab.title('Difference Between Heads and Tails')
    #pylab.xlabel('Number of Flips')
    #pylab.ylabel('Abs(#Heads - #Tails')
    #pylab.plot(xAxis, diffs)
    #pylab.figure()
    #pylab.plot(xAxis, ratios)
    #pylab.title('Heads/Tails Ratios')
    #pylab.xlabel('Number of Flips')
    #pylab.ylabel('Heads/Tails')
    #pylab.figure()
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails')
    pylab.plot(xAxis, diffs, 'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.plot(xAxis, ratios, 'ro')
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.semilogx()

flipPlot(4, 20)
pylab.show()

