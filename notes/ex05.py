# # # 05 - Efficiency - Time&Space

# # count number of basic steps
# # steps take constant time
# # Random Access Memory (RAM) - sequential, constant time

# # Best case - minimum running time over all possibles input
# # Worst case - maximum running time over all possibles input - focus 
# # Average case (expected)

## Complexity
## Factorial - iterative
#def f(n):
	#assert n >= 0	#1 step
	#answer = 1		#1 step
	#while n > 1:	#n steps
		#answer += 1	#n steps
		#n -= 1		#n steps
	#return answer	#1 step
					##3 + 3*n steps // 3*n - growth steps  // n - asynptotic growth
					##Big Oh - O(n) = order of growth (in this case n)
					##Ex: f(x) E O(x^2) - function f grows no faster than the quadratic polynomial x^2
##Order of growth:	
## O(1) = constant
## O(logn) = logarithmic
## O(n) = linear
## O(nlogn) = log linear
## O(n^c) = polynomial
## O(c^n) = exponential
## O(c^n) > O(n^c)

#Factorial - recursive
#def fact(n):
	#assert n >= 0				#fact(n) E O(n) 
	#if n <= 1:					#same order as iteration
		#return n				#recursive x iterative don't affect directly in the efficiency
	#else:
		#return n*fact(n - 1)

 #def g(n):
	 #x = 0
	 #for i in range(n):			#n times
		 #for j in range(n):			#n times - start with the inner loop
			 #x += 1				#g(n) E O(n^2)
	 #return x
	
 #def h(x):
	 #assert type(x) == int and x >= 0
	 #answer = 0
	 #s = str(x)
	 #for c in s:					#n times
		 #answer += int(c)		#h(x) E O(log2n) where n is the number of digits in x
	 #return answer
	
 #def search(L, e):
	 #global numCalls
	 #for elem in L: 
		 ## numCalls += 1
		 #if elem == e: 			#O(n) where n is len(L)
			 #return True 
	 #if elem > e: 
		 #return False 
	 #return False 
	
	
def bSearch(L, e, low, high):
	global numCalls
	numCalls += 1 				#O(n) where n is log2(len(L))
	if high - low < 2:
		return L[low] == e or L[high] == e
	mid = low + int((high - low)/2)
	if L[mid] == e:
		return True 
	if L[mid] > e:
		return bSearch(L, e, low, mid - 1)
	else: 
		return bSearch(L, e, mid + 1, high) 

def search(L, e):
	return bSearch(L, e, 0, len(L) - 1) 
	
L = range(100)
numCalls = 0 
print search(L, 3)
print numCalls 

L = range(200)
numCalls = 0 
print search(L, 3)
print numCalls 

L = range(400)
numCalls = 0 
print search(L, 3)
print numCalls 

L = range(1000)
numCalls = 0 
print search(L, 3)
print numCalls 

L = range(10000)
numCalls = 0 
print search(L, 3)
print numCalls 

 # O(1) = O(2^1000) -> constant: O(1)
 # Does not depend on the input size, but in the algorithms




