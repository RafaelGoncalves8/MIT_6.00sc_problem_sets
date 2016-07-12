# # # 04 - Debugging

# # Floats - Binary:
#0.1 = decimal: 1*10^-1 | binary: ~ 0.0001100110011001100110011...
#x = 0.0
#numItens = 100000
#for i in range(numItens):
	#x += 0.1
#print x			#binary aproximation
#print repr(x)	#real binary value
#print 10.0*x == numItens

#def close(x, y, epsilon = 0.00001):
	#return(x-y) < epsilon
	
#if close(10.0*x, numItens):
	#print 'Good Enough'
	
# # # Debugging - print:
# # Not to eliminate one bug quickly
# # Is to move towards a bug-free program
#def isPal(x):
	#"""requires x to be a list
#returns True if the list is a palindrome; False otherwise"""
	#if type(x) == str:
		#x = list(x)
	#assert type(x) == list
	#temp = x[:]
	#temp.reverse()
	#print 'x is = %r' % x		#checking
	#print 'temp is %r' % temp
	#if temp == x:
		#return True 
	#else: 
		#return False 

#def silly(n):
	#"""requires: n is an int > 0
 #Gets n inputs from user
 #Prints 'Yes' if the inputs are a palindrome; 'No' otherwise"""
	#assert type(n) == int and n > 0
	#result = []
	#for i in range(n):
		#elem = raw_input('Enter something: ')
		#result.append(elem)
		#print result 	#debugging tool for checking errors
	#if isPal(result):
		#print 'Is a palindrome'
	#else: 
		#print 'Is not a palindrome' 


#def isPalTest():
	#L = [1, 2]
	#result = isPal(L)
	#print 'Should print False:', result
	#L = [1, 2, 1]
	#result = isPal(L)
	#print 'Should print True:', result 
	
#def PalTest():
	#assert isPal('a') == True
	#assert isPal('ab') == False
	#assert isPal('aa') == True
	#assert isPal('aba') == True
	#assert isPal('abc') == False
	#assert isPal('abba') == True
	#assert isPal('abca') == False
	#print 'Passed in all tests'
	
 #isPalTest()
#PalTest()

 ### Pseudo-code:
 ##Prime numbers:
  ##- test number if equal to 2, 3
  ##- If equal return true
  ##- while x less then sqrt(n)
	 ##test if x evenly divides n (n%x ==0)
		 ##if it does return false
	 ##add 2 to x

def Primary(n):
	if n <= 3:
		if n == 2 or n ==3:
			return True
		else:
			return False
	else:
		for divisor in range (2, int(n**0.5)+1):
			if n%divisor == 0:
				return False
		return True
print Primary(1)
print Primary(2)
print Primary(3)
print Primary(4)
print Primary(5)
print Primary(5121)
