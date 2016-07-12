# # # 02 - Objects:
# # Tuples, Lists, Strings and Dictionaries

# # Tuples (starts at index 0)

#tuple_of_numbers = (3.14159, 2, -1, 0.5, 240)
#tuple_of_strings = ("What","is","my","name?")
#tuple1 = ((1, 2, 3), 'I', 'B', 0.5)
#print tuple_of_numbers[0:4]
#print tuple_of_strings[-2]
#print len(tuple_of_numbers) #length of a tuple
#tuple = tuple_of_numbers + tuple_of_strings
#print tuple
#print tuple[:]
#print tuple1[0]
#print tuple[:-3]
#print tuple[4:]
#print tuple1[:]
#tuple_of_numbers = tuple_of_numbers + (100, 200, 300)
#print tuple_of_numbers

# # Strings

#A=(50)
#print A
#A = (50,)
#print A
#print A[0]
#name = 'Rafael Goncalves'
#print name[1]
#print name[2:10]
#print name.find('el')
#for letter in name:
	#print letter
#name = name.replace('Rafa','Gabri')
#print name

# # Lists (mutable tuple (?) ) - side effects

#list1 = ['hey', "I'm", "a", "list"]
#list2 = [1, 2, 3]
#print list1
#print list2
#list1.append("appended")	#mutating list
#print list1
#list2.append(list1)
#print list2
#for e in list1:
	#print e
#list_a = [1, 2, 3, 4, 5]
#list_b = [2, 6, 10]
#list_c = [1, 3]
#for i in list_a:
	#if i in list_b:
		#list_a.remove(i) 
	#print list_a
#print list1
#list1.sort() #put it in alphabetical order
#print list1

#L1 = [1, 2]
#L2 = [L1, L1]
#print L2
#L1.remove(2)
#L1.append(3)
#print L2
#L1 = ['abc']
#print L1
#print L2

#def copyList (LSource, LDest):
	#for e in LSource:
		#LDest.append(e)
		#print "LDest:", LDest
	#return LDest
#L1 = [1, 2, 3]
#L2 = [] 
#copyList(L1, L2)
#print "L1:", L1
#print "L2:", L2
#print copyList(L1, L1) #Alias: one object with multiple names

 
# Dictionaries -  the keys can be any immutable type (unordered)

#Dict = {1: 'one', 2: 'two', 'pi': 3.14159} #set of <key, values> pairs
#print Dict['pi']
#print Dict
#Dict[1] = 'uno'
#print Dict

# #EnglishtoFrench
#EtoF = {'bread': 'du pain', 'wine': 'du vin', \
#'eats': 'mange', 'drinks': 'bois', 'likes': 'aime'}
#print EtoF
#print EtoF.keys()
#print EtoF.keys
#del EtoF['bread']
#print EtoF

#def translateWord(word, dictionary):
	#if word in dictionary:
		#return dictionary[word]
	#else:
		#return word
		
#def translate(sentence):
	#translation = ''
	#word = ''
	#for c in sentence:
		#if c != ' ':
			#word = word + c
		#else:
			#translation = translation + ' '\
			#+ translateWord(word, EtoF)
			#word = ''
	#return translation[1:] + ' ' + translateWord(word, EtoF)
	
#print translate('John eats bread')
#print translate('Steve drinks wine')
#print translate('John likes bread')

# # Tuple:
#print """\n Tuples \n"""
#tupA = (1, 2, 3)
#tupB = (tupA, "a", 1.12, [2, 4, 6])

#print tupB
#print tupA[0]
#print tupA[0:2]
#print tupA[0:3]
#print tupA[:]

## # List:
#print """\n Lists \n"""
#listA = [0, 1, 2]
#listB = [1.2, listA]
#print listB
#listA.append(3)
#print listA
#listA.remove(1) #remove specified element
#print listA
#listA.pop(-1) #remove element 'n' in .pop(n)
#print listA
#listA.extend([4,5])
#print listA
#print listA[0:2]
#listA.pop(-1), listA.pop(-1)
#listA.append([4,5])
#print listA
#print listB
#listC = [[]]*10 #10 empty elements
#print listC
#listX = [1, 2, 3]
#listY = listX	 #copy pointers (references)
#listZ = listX[:] #copy elements
#listX.pop(0)
#print listY
#print listZ

# # Matrix:
#print """\n Matrix \n"""
#M = [['A','B'], ['C','D'], ['E','F']] #matrix 3x2
#print M[1]
#print M[0][1]
#print M[2][0]

# # Dictionaries
#print """\n Dictionaries \n"""
#D1 = {'key1': 1,		#keys -> immutable // values -> can be mutable
#'key2': 2,
#'key3': 3}
#print D1
#if 'key1' in D1:
	#print D1['key1']
#del D1['key1']
#print D1
#keys = D1.keys()
#print keys
#keys.sort()
#print keys
#print D1.items() #turn pair key/value as a tuple
