# # # 08 - Class:
# # Objected-Oriented programming
# # Module = collection of functions. Ex: import math // math.log (function log into file math)
# # Class = collection of data + functions. Ex: L.append(e) - associate attribute with object 
# #                                                           L = object / append(e) = message(attribute) to the obj(of class 'List') L
# # Method = Function associated with and object(of given class. Ex: methods for ints, floats, lists, dicts. In the example, the method is append
# # Lists, Dicts = Built in classes
# # Libraries = collection of classes
# # Abstract data type(class)
# # Inheritance = sub-classes have common attributes in relation of the super-classes


class inSet(object):
	#set of integers
	def __init__(self):
		"""Create an empty set of integers"""
		self.numBuckets = 47
		self.vals = []
		for i in range(self.numBuckets):
			self.vals.append([])
		
	def hashE(self, e):
		return abs(e)%len(self.vals)
		
	def insert(self, e):
		"""assumes e is an integer and inserts e into self"""
		for i in self.vals[self.hashE(e)]:
			if i == e: return
		self.vals[self.hashE(e)].append(e)
		
	def member(self, e):
		"""assumes e is an integer
		returns True if e is in self, and False otherwise"""
		return e in self.vals[self.hashE(e)]
		
	def __str__(self):
		"""Returns a string representation of self"""
		elems = []
		for bucket in self.vals:
			for e in bucket: elems.append(e)
		elems.sort()
		result = ''
		for e in elems: result = result + str(e) + ','
		return '{' + result[:-1] + '}'
		
def test1():
	s = inSet()
	for i in range(40):
		s.insert(i)
	print s.member(14)
	print s.member(41)
	print s
	print s.vals #Evil
	
# test1()
	
# # Data hiding - no direct acces to instance variables and class variables

import datetime

class Person(object):
	def __init__(self, name):
		self.name = name
		try:
			firstBlank = name.rindex(' ')
			self.lastName = name[firstBlank + 1:]
		except:
			self.lastName = name
		self.birthday = None
	def getLastName(self):
		return self.lastName
	def setBirthday(self, birthDate):
		assert type(birthDate) == datetime.date
		self.birthday = birthDate
	def getAge(self):
		assert self.birthday != None
		return (datetime.date.today() - self.birthday).days
	def __lt__(self, other):
		if self.lastName == other.lastName:
			return self.name < other.name
		return self.lastName < other.lastName
	def __str__(self):
		return self.name
		
# A = Person('Rafael Goncalves')
# B = Person('Another Person')
# print A
# print A.getLastName()
# A.setBirthday(datetime.date(1997, 8, 30))
# B.setBirthday(datetime.date(1998, 4, 21))
# print A.getAge()
# print A < B
# print B < A
# list1 = [B, A]
# for p in list1: print str(p)
# list1.sort()
# for p in list1: print str(p)

# # Inherits properties of super-class

class MITPerson(Person):
	nextIdNum = 0
	def __init__(self, name):
		Person.__init__(self, name)
		self.idNum = MITPerson.nextIdNum
		MITPerson.nextIdNum += 1
	def getIdNum(self):
		return self.idNum
	def __lt__(self, other):
		return self.idNum < other.idNum		#override properties of super class (Person)
	def isStudent(self):
		return type(self) == UG or type(self) == G
		
# p1 = MITPerson('Rafael Goncalves')
# print p1, p1.getIdNum()
# p2 = MITPerson('Jhon Guttag')
# print p2, p2.getIdNum()
# p3 = MITPerson('Jhon Guttag')
# print p3, p3.getIdNum()
# p4 = Person('Another People')
# print 'p1 < p2 =', p1 < p2
# print 'p3 < p2 =', p3 < p2
# print '__lt__(p1, p2) =', Person.__lt__(p1, p2)
# print 'p1 == p4 =', p1 == p4
# print 'p4 < p3 =', p4 < p3 #__lt__ associated w/ p4 (Person class)
# # print 'p3 < p4 =', p3 < p4 # __lt__ associated w/ p3 (MITPerson class) - Error: this is a Person not a MITPerson so don't have IdNum
class UG(MITPerson):
	def __init__(self, name):
		MITPerson.__init__(self, name)
		self.year = None
	def setYear(self, year):
		if year > 5:
			raise OverflowError('Too Many')
		self.year = year
	def getYear(self):
		return self.year
		
class G(MITPerson):
	pass		#have all normal properties that an MITPerson has
	
# ug1 = UG('Rafael Goncalves')
# ug2 = UG('Jane Doe')
# p3 = MITPerson('Sue Yuan')
# print ug1			#pick __str__ from super classes
# print ug1 < p3
# print ug2 < ug1
# print ug1 == ug2
# p4 = G('Person')
# print type(p4)
# print p4 == G

class CourseList(object):
	def __init__(self, number):
		self.number = number
		self.students = []
	def addStudent(self, who):
		if not who.isStudent():
			raise TypeError('Not a student')
		if who in self.students:
			raise ValueError('Duplicate Student')
		self.students.append(who)
	def remStudent(self, who):
		try:
			self.students.remove(who)
		except:
			print str(who) + 'not in ' + self.number
	def allStudents(self):
		for s in self.students:
			yield s
	def ugs(self):
		indx = 0
		while indx < len(self.students):
			if type(self.students[indx]) == UG:
				yield self.students[indx]
			indx += 1

# # # Creating a Person (exemple on OOP):

# # Non OO programming:
def make_person(name, age, height, weight):
	person = {}
	person['name'] = name
	person['age'] = age
	person['height'] = height
	person['weight'] = weight
	return person
	
def get_name(person):
	return person['name']
	
def set_name(person, name):
	person['name'] = name

def get_age(person):
	return person['age']
	
def set_age(person, age):
	person['age'] = age
	
def get_height(person):
	return person['height']
	
def set_height(person, height):
	person['height'] = height
	
def get_weight(person):
	return person['weight']
	
def set_height(person, weight):
	person['weight'] = weight
	
def print_person(person):
	print 'Name:', get_name(person), ', Age:', get_age(person), ', Height:', get_height(person), ', Weight:', get_weight(person)

# mitch = make_person('Mitch', 32, 70, 200)
# sarina = make_person('Sarina', 25, 65, 130)
# print_person(mitch)
# set_age(mitch, 25)
# print "New age: %d" % get_age(mitch)
# # Problems:
# print type(mitch)	#don't mean anything, any dict can be used for the functions
# not_a_person = {'RandomJunk': 'Junk', 'Junk':'RandomJunk'}
# print type(mitch) == type(not_a_person)

# # OO Programming (classing):

class person(object):
	def __init__(self, name, age, height, weight):	#automatic calls this function when you defines a new 'person'
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight
	
	def get_name(self): 	#this method is called accessor or getter
		return self.name
		
	def set_name(self, name):	#mutator or setter
		self.name = name
		
	def get_age(self):
		return self.age
	
	def set_age(self, age):
		self.age = age
		
	def get_height(self):
		return self.height
	
	def set_height(self, height):
		self.height = height
		
	def get_weight(weight):
		return self.weight
	
	def set_weight(self, weight):
		self.weight = weight
		
	def __str__(self):	#underbar methods have special significance in Python
		return 'Name: ' + self.name + ', Age: ' + str(self.age) + ', Height: ' + str(self.height) + ', Weight: ' + str(self.weight)
		
	def __eq__(self, other):
		return self.name == other.name

# mitch = person('Mitch', 32, 70, 200)
# sarina = person('Sarina', 25, 65, 130)
# print mitch
# mitch.set_age(25)
# print "New age:" + str(mitch.get_age())
# print type(mitch)
# print mitch == sarina

# print mitch.get_age()
# print person.get_age(mitch) #<- meaning of the self parameter. Python automatically puts the object name in the method

# # Shapes

class Shape(object):
	def area(self):
		raise NotImplementedError
	def perimeter(self):
		raise NotImplementedError
	def __eq__(self, other):
		return self.area() == other.area()
	def __lt__(self, other):
		return self.area() < other.area()
	
class Rectangle(Shape):
	def __init__(self, side1, side2):
		self.side1 = side1
		self.side2 = side2
	def area(self):
		return self.side1 * self.side2
	def perimeter(self):
		return 2 * self.side1 + 2 * self.side2
	def __str__(self):
		return 'Rectangle(%d x %d)' % (self.side1, self.side2)
		
class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
	def area(self):
		return 3.14159 * self.radius ** 2
	def perimeter(self):
		return 2.0 * 3.14159 * self.radius
	def __str__(self):
		return 'Circle(%d)' % self.radius
		
class Square(Rectangle):
	def __init__(self, side):
		Rectangle.__init__(self, side, side)
	def __str__(self):
		return 'Square(%d)' % self.side1
		
# s = Shape()
# print s.area()

r = Rectangle(2, 8)
sq = Square(4)
c = Circle(10)
# print 'Rectangle area:', r.area()
# print 'Square area:', sq.area()
# print 'Circle area:', c.area()

# print 'Rectangle(2, 8) == Square(4):', r == sq
# print 'Rectangle(2, 8) < Square(4):', r < sq

# print 'Circle(10) == Square(4):', c == sq
# print 'Circle(10) < Square(4):', c < sq

# list_of_shapes = [c, sq, r]
# for shape in list_of_shapes:
	# print shape.area()
	
# for shape in list_of_shapes:
	# print shape
	
# list_of_shapes.sort()
# print '---'
# for shape in list_of_shapes:
	# print shape