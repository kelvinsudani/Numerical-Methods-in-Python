
from numpy import dot
def LUdecomp(a):
        n = len(a)
        for k in range(0,n-1):
            for i in range(k+1,n):
                if a[i,k] != 0.0:
                    lam = a [i,k]/a[k,k]
                    a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                    a[i,k] = lam
        return a
def LUsolve(a,q):
        n = len(a)
        for k in range(1,n):
            q[k] = q[k] - dot(a[k,0:k],q[0:k])
        for k in range(n-1,-1,-1):
            q[k] = (q[k] - dot(a[k,k+1:n],q[k+1:n]))/a[k,k]
        return q


# Example
from numpy import array
a = array([[ 1.44, -0.36, 5.52, 0.0], \
        [-0.36, 10.33, -7.78, 0.0], \
        [ 5.52, -7.78, 28.40, 9.0], \
        [ 0.0, 0.0, 9.0, 61.0]])

b = array([0.04, -2.15, 0.0, 0.88])

temp = LUdecomp(a)
ans = LUsolve(temp,b)
print 'answer = ',ans