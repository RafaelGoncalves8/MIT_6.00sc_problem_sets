# # # 01 - Solving problems - Iteration
# # Brute force/bissection search functions (iterative)
# # find root squares

# #Brute Force O(N)

#x = int(raw_input('Enter an integer:'))
#ans=0
#while ans*ans*ans < abs(x):
	#ans=ans+1
	#print "current guess = ", ans
#if ans*ans*ans != abs(x):
	#print x, " is not a perfect cube"
#else:
	#if x<0:
		#ans=-ans
	#print 'cube root of ' + str(x) + ' is ' + str(ans)
#raw_input('end')

#x = int(raw_input('Enter an integer:'))
#for ans in range(0,(x+1)):
	#if ans**3 == abs(x):
		#break
#if ans**3 != abs(x):
	#print(x, "isn't a perfect cube")
#else:
	#if x<0:
		#ans=-ans
	#print 'cube root of ' + str(x) + ' is ' + str(ans)
#raw_input('end')

#x=int(raw_input('Choose a number:'))
#epsilon = 0.01
#numGuesses=0
#ans=0.0
#while abs(ans**2 - x) >= epsilon and ans <= x:
	#ans += 0.00001
	#numGuesses += 1
#print 'numGuesses=', numGuesses
#if abs(ans**2-x) >= epsilon:
	#print 'Failed on square root of ', x
#else:
	##print ans, 'is close to square root of ', x
	#print "%.2f is close to square root of %d" % (ans, x)
#raw_input('End')


# # Bisection Search O(log N)

#x = int(raw_input('Choose a number:'))
#epsilon = 0.01
#numGuesses = 0
#low = 0.0
#high = x
#ans= (high+low)/2.0
#while abs(ans**2 - x) >= epsilon and ans<= x:
	##print 'low', low, 'high' high, 'ans' ans
	#numGuesses += 1
	#if ans**2 < x:
		#low=ans
	#else:
		#high=ans
	#ans= (high+low)/2.0
#print 'numGuesses =', numGuesses
#print '%.2f is close to square root of %d' % (ans, x)
#raw_input('end')

#x = 0.5  #when x<0 
#epsilon = 0.01
#numGuesses = 0
#low = 0.0
#high = max(x, 1.0) #You need to change the high variable
#ans= (high+low)/2.0
#while abs(ans**2 - x) >= epsilon and ans<= x:
	## print 'low', low, 'high' high, 'ans' ans
	#numGuesses += 1
	#if ans**2 < x:
		#low=ans
	#else:
		#high=ans
	#ans= (high+low)/2.0
#print 'numGuesses =', numGuesses
#print ans, ' is close to square root of ', x
#raw_input('end')


# # # 02 - Decomposition and Abstraction

#def withinEpsilon(x, y, epsilon):                   #function
	#"""	x, y, epsilon floats. epsilon > 0
		#returns True if x is within epsilon of y - O(1)""" #description
	#return abs(x-y) <= epsilon

#print withinEpsilon(2,3,1)
#val = withinEpsilon(2,3,0.5)
#print val

#def f(x):   #x can assume more than one value, depending on the stack (Main, f(), etc... ) - O(1)
	#x=x+1
	#print 'x = ', x
	#return x

#x =	3
#z = f(x)
#print 'z =', z   #z will print x of f(x) function, that is x+1 that is 4
#print 'x =', x   #x will print the old x that is 3 because it's no longer in the f() stack

#def isEven(i):
	#"""assumes i a positive int
	#returns True if i is even, otherwise False"""
	#return i%2 == 0

#def findRoot(pwr, val, epsilon):
	#"""assumes pwr an int; val, epsilon floats
	#pwr and epsilon > 0
	#if it exists,
		#returns a value within epsilon of val**pwr
		#otherwise returns None"""
	#assert type(pwr) == int and type(val) == float and type(epsilon) == float
	#assert pwr > 0 and epsilon > 0
	#if isEven(pwr) and val < 0:
		#return None
	#low = -abs(val)
	#high = max(abs(val), 1.0)
	#ans = (high + low)/2.0
	#while not withinEpsilon (ans**pwr, val, epsilon):
		##print 'ans =', ans, 'low =', low, 'high =', high
		#if ans**pwr < val:
			#low = ans
		#else:
			#high = ans
		#ans = (high + low)/2.0
	#return ans

#def testFindRoot(val):	
	#"""val float, epsilon float, pwr positive int"""
	#for pwr in (1, 2, 3, 4, 5):
		#ans = findRoot(pwr, val, 0.001)
		#if ans == None:
			#print 'The answer is imaginary.'
		#else: 
			##print ans, 'to the power', pwr, 'is close to', val
			#print '%.2f to the power %d is close to %.2f' % (ans, pwr, val)

#val = float(raw_input('Choose a number:'))                   
#testFindRoot(val)

			
#sumDigits = 0
#for c in str(1952):
	#sumDigits += int(c)
#print sumDigits

#x=100
#divisors = ()
#for i in range(1,x):
	#if x%i == 0:
		#divisors = divisors + (i,)

#print divisors		
#print divisors[0] + divisors[1]
#print divisors [2:4]

