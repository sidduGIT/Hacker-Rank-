import numpy
n=int(input())
A=[input().split() for _ in range(n)]
A=numpy.array(A,float)
print(numpy.linalg.det(A))
