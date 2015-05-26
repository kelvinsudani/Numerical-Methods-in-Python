# -*- coding: cp1252 -*-
## Gauss elimination.

from numpy import dot
def gaussElimin(a,b):
	n = len(b)
	for k in range(0,n-1):
		for i in range(k+1,n):
			if a[i,k] != 0.0:
				f = a [i,k]/a[k,k]
				a[i,k+1:n] = a[i,k+1:n] - f*a[k,k+1:n]
				b[i] = b[i] - f*b[k]
	# Back substitution
	for k in range(n-1,-1,-1):
		b[k] = (b[k] - dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
	return b
# Example
from numpy import array
a = array([[ 1.44, -0.36, 5.52, 0.0], \
        [-0.36, 10.33, -7.78, 0.0], \
        [ 5.52, -7.78, 28.40, 9.0], \
        [ 0.0, 0.0, 9.0, 61.0]])

b = array([0.04, -2.15, 0.0, 0.88])

ans = gaussElimin(a,b)
print 'answer = ',ans