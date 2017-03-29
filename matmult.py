"""
Title:
Experimental Backing for Conjecture that Column-Swaping Operator
F: S -> S, for Compact Convex S with Vector Metric D,  with
Contracting Operator A, Satisfy Brower Fixed Point Theorem.

Author: Aditya S. Chanda

"""

def inner_product(rowvector, columnvector):
     'inner product of two vectors.'
     sum = 0
     for i in xrange(len(rowvector)):
            sum += rowvector[i] * columnvector[i]
     return sum

def Matrix_Multiplication(M, v):
     """
     Matrices are of the form M=[[1,2,3],[4,5,6],[7,8,9]].
     
     In this function we are assuming that every row in M is a
     row vector M[i].
     
     We're simply finding the inner product of M[i] and v
     """
     return [inner_product(i, v) for i in M]

def Column_Swap(M,v,n):
	"""
	Given some matrix M and some vector v and some integer
	index n, we want to swap out the n mod len(M) column
	with vector v.
	
	In the context of this algorithm, n is in 
	interval [1,infinity], where [1,infinity] is a subset
	of the integers, rather than the reals.
	
	n is supposed to be the exponent that matrix M is
	raised to.
	
	If it's zero, then v is multiplied by the identity
	matrix.
	
	For Mv = w, where w is some other vector, the implied
	value of n is 1.
	
	"""
	swap_index = int((n-1)%len(M))
	i = 0
	while i<len(v):
		M[i][swap_index] = v[i]
		i = i + 1
	return M

A = [[1,0,0],[0,1,0],[0,0,1]]
v = [float(1)/float(3),float(1)/float(3),float(1)/float(3)]
power = 1

while power<20:
	print v
	v_buffer = v
	v = Matrix_Multiplication(A,v)
	A = Column_Swap(A,v_buffer,power)
	power = power + 1

