# # # 09 - Generators and random walks:


from ex08 import *

# # # Generators:
# # Yield => generator
# # function that remembers the point in the function body where it last returned, plus local variable
# # generates data from a 'list' that you'll only need once
		
m1 = MITPerson('Barbara Beaver')			
ug1 = UG('Jane Doe')
ug2 = UG('John Doe')
g1 = G('Mitch Peabody')
g2 = G('Ryan Jackson')
g3 = G('Sarina Canelake')
SixHundred = CourseList('6.00')
SixHundred.addStudent(ug1)
SixHundred.addStudent(g1)
SixHundred.addStudent(ug2)
# try:
   # SixHundred.addStudent(m1)
# except:
   # print 'Whoops'
# print SixHundred #Perhaps not what one expected
# SixHundred.remStudent(g3)
# print 'Students'
# for s in SixHundred.allStudents():
   # print s
   
# print 'Students Squared'
# for s in SixHundred.allStudents():
   # for s1 in SixHundred.allStudents():
	   # print s, s1
	   
# print 'Undergraduates'
# for u in SixHundred.ugs():
   # print u
   
# # # Analytic methods:
# # predict behavior, given the conditions and parameters

# # # Simulation methods:
# # systems not mathematical trackable

# # Simulation:
# build a method that gives useful information about the behavior of systems
# approximation to reality 
# descriptive, not prescript
# useful when its difficult to create a matematical module

# # Random Walks

import random

class Location(object):
	def __init__(self, x, y):
		"""x and y are floats"""
		self.x = x
		self.y = y
	def move(self, deltaX, deltaY):
		"""deltaX and deltaY are floats"""
		return Location(self.x + deltaX, self.y + deltaY)
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def distFrom(self, other):
		ox = other.x
		oy = other.y
		xDist = self.x - ox
		yDist = self.y - oy
		return (xDist**2 + yDist**2)**0.5
	def __str__(self):
		return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]
	

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)
    def __str__(self):
        return 'This drunk is named ' + self.name

def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))

hommer = Drunk('Hommer')
field = Field()
location = Location(0, 0)
field.addDrunk(hommer, location)

#walk(field, hommer, 10)
#print field.getLoc(hommer)
#
#walk(field, hommer, 10)
#print field.getLoc(hommer)
#
#walk(field, hommer, 10)
#print field.getLoc(hommer)
	
def simWalks(numSteps, numTrials):
    homer = Drunk('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances

def drunkTest(numTrials):
    for numSteps in [10, 100, 1000, 10000, 100000]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print '  Mean =', sum(distances)/len(distances)
        print '  Max =', max(distances), 'Min =', min(distances)
		
#sim = simWalks(10, 5)
#print sim
#
#sim1 = drunkTest(10)
#
#print sim1

