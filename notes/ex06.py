# # # 06 - Efficiency - Sorting

# # # Memory
# # Indirection (same length parts with pointers for varied length pats)

# # # Efficient search
# # Sort L - O(?)
# # Binary Search - O(log(lenL))
# # O(?) + O(log(lenL)) < O(L) - impossible, because Sort L = O(L)

# # # Amortized Complexity
# # Sort once; search various times,
# # then: O(sort(L)) + O(K*log(lenL)) < K*O(L) = True



# # # Selection Sort:
# # prefix, suffix, invariant
# # O(n^2)

#def selSort(L):
	#"""Assumes that L is a list of elements that can be compared using >.
	#Sorts L in ascending order"""
	#for i in range(len(L) - 1):
		#minIndx = i 	#invariant
		#minVal= L[i]		#prefix
		#j = i + 1			#suffix
		#while j < len(L):
			#if minVal > L[j]:
				#minIndx = j
				#minVal= L[j]
			#j += 1
			#print L
		#temp = L[i]
		#L[i] = L[minIndx]
		#L[minIndx] = temp 
		#print 'Partially sorted list:', L
	
#L = [4, 5, 4 ,2 ,9, 11, 12, 1]
#selSort(L)

# # # Merge Sort:
# # Divide&Conquer
# # Threshold input size, n0, smallest problem
# # How many instances at each division
# # Combine the sub solutions


def merge(left, right, lt):
	"""Assumes left and right are sorted lists.
	It defines an ordering on the elements of the lists.
	Returns a new sorted(by lt) list containing the same elements
	as (left + right) would contain."""
	result = []
	i, j = 0, 0
	while i < len(left) and j< len(right):
		if lt(left[i], right[j]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while (i<len(left)):
		result.append(left[i])
		i += 1
	while (j < len(right)):
		result.append(right[j])
		j += 1
	return result

def sort(L, lt = lambda x, y: x < y):
	"""Returns a new sorted list containing the same elements as L"""
	if len(L) < 2: #threshold
		return L[:]
	else:
		middle = int(len(L)/2)
		left = sort(L[:middle], lt)
		right = sort(L[middle:], lt)
		print "About to merge", left, "and", right
		return merge(left, right, lt)
		
#L = [4, 5, 4 ,2 ,9, 11, 12, 1]
#newL = sort(L)
#print L
#print newL

def lastNameFirstName(name1, name2):
	import string
	name1 = string.split(name1, ' ')
	name2 = string.split(name2, ' ')
	#print name1, name2
	#print name1[1][0] < name2[1][0]
	if name1[1] != name2[1]:
		return name1[1] < name2[1]
		#print name[1], name2[1]
		#print name1[1] < name2[1]
	else: 
		return name1[0] < name2[0]
		#print name[0], name2[0]
		#print name1[0] < name2[0]

def firstNameLastName(name1, name2):
	import string  
	name1 = string.split(name1, ' ')
	name2 = string.split(name2, ' ')
	print name1, name2
	if name1[0] != name2[0]:
		return name1[0] < name2[0]
	else: 
		return name1[1] < name2[1] 

L = ['John Guttag', 'Tom Brady', 'Chancellor Grimson', 'Gisele Brady',
'Big Julie']
newL = sort(L, lastNameFirstName)
print 'Sorted list =', newL
newL = sort(L, firstNameLastName)
print 'Sorted list =', newL 
