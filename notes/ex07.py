# # # 07 - Hashing
# # Hash: converts i into a int in range(0, k)
# # Hash is many-to-one
# # Colision: when two values matches the same hash.
## Solution: linear rehash (list of entries in each hash)

numBuckets = 47

def create():
	global numBuckets
	hSet = []
	for i in range(numBuckets):
		hSet.append([])
	return hSet
	
#def hashElem(e):
	#global numBuckets
	#return e%numBuckets
	
def insert(hSet, i):
	hSet[hashElem(i)].append(i)
	
def remove(hSet, i):
	newBucket = []
	for j in hSet[hashElem(i)]:
		if j != i:
			newBucket.append(j)
	hSet[hashElem(i)] = newBucket
	
def member(hSet, i):
	return i in hSet[hashElem(i)]
	
# # Test
numBuckets = 3
def test1(): 
	s = create() 
	for i in range(40): 
		insert(s, i) 
	insert(s, 325) 
	insert(s, 325) 
	insert(s, 987654321) 
	print s 
	#assert False
	print member(s, 325) 
	remove(s, 325) 
	print member(s, 325) 
	print member(s, 987654321) 
	
#test1()

def hashElem(e):
	global numBuckets
	if type(e) == int:
		val = e
	if type(e) == str:
		# convert e to an int
		val = 0
		shift = 0
		for c in e:
			val = val + shift*ord(c)
			shift += 1
	return val%numBuckets
	
def test2():
	d = create()
	strs = ['ab', 'ba', '32a', 'big dog', 'small bird']
	for s in strs:
		insert(d, s)
	for i in range(40):
		insert(d, i)
	print d
	print member(d, 'small bird')
	print member(d, 'big bird')
	remove(d, 'small bird')
	print d
	
#test2()

# # # Exceptions

def readVal(valType, requestMsg, errorMsg):
	numTries = 0
	while numTries < 4:
		val = raw_input(requestMsg)
		try: 
			val = valType(val)
			return val
		except ValueError:
			print(errorMsg)
			numTries += 1
	raise TypeError('num tries exceeded')
	
print readVal(int, 'Enter int: ', 'Not an int.') 

try: 
	readVal(int, 'Enter int: ', 'Not an int.') 
except TypeError, s: 
	print s 
