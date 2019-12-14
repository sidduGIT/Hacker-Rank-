import numpy

a=numpy.array([1,2,3,4,5,6])
print(a)

b=numpy.array([1,2,3,4,5,6],float)
print(b[1])
'''
Task

You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.

Input Format

A single line of input containing space separated numbers.

Output Format

Print the reverse NumPy array with type float.

Sample Input

1 2 3 4 -8 -10

Sample Output

[-10.  -8.   4.   3.   2.   1.]
'''

import numpy
arr=list(map(int,input().split()))
print(arr)
result=numpy.array(arr,float)[::-1]
print(result)
