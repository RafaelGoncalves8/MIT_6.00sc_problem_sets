# # # 03 - Solving problems - Recursion
# # Divide and conquer (small parts are easier to solve break the code into small parts) 
	
# # Recursion (way of describing problems and solutions)

#def Expo(num,n): 	#exponential recursively - O(n)
	#if n == 0:
		#ans = 1
	#else:
		#ans = num*Expo(num, n-1)
	#return ans
	
#num = int(raw_input('Choose a number:'))
#n = int(raw_input("Chose the exponential:"))

#print Expo(num, n)

#def hanoi(n, S, T, B):
	#assert n>0
	#if n == 1:
		#print "move %s to %s" % (S, T)
	#else: 
		#hanoi(n-1, S, B, T)
		#hanoi(1, S, T, B)
		#hanoi (n-1, B, T, S)
	
#num = int(raw_input("Number of discs in hanoi towers:"))
#hanoi(num, 'Source', 'Target', 'Buffer')
	
#def toChars(s):
	#s = s.lower()
	#ans = s 
	#return ans

#def isPal(s):
	#if len(s) <= 1:
		#return True 
	#else: 
		#return s[0] == s[-1] and isPal(s[1:-1])
		
#def isPalindrome(s):
	#"""Returns True if s is a palindrome and False otherwise"""
	#return isPal(toChars(s))
	
#print isPalindrome('Guttag')
#print isPalindrome('Guttug')
#print isPalindrome('Able was I ere I saw Elba')
#print isPalindrome('Are we not drawn onward, we few, drawn onward to new era?')
#print isPalindrome(raw_input('Wich sentence do you want to know if is a palindrome?'))

##Factorial
##Recursive case -> n! = n(n-1)! 
##Base case -> if n == 0, return 1

#def Factorial(n):
	#if n==0:
		#return 1  ##base case
	#else:
		#return n*Factorial(n-1) #recursive case
		
#num = int(raw_input('Give an integer:'))
#print "Factorial of %d is:" % num, Factorial(num)
