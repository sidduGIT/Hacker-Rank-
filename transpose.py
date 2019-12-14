import numpy

arr=numpy.array([[1,2,3],
                 [4,5,6]])
print('original array')
print(arr)
print('shape')
print(numpy.shape(arr))
trans_arr=numpy.transpose(arr)
print('transpose')
print(trans_arr)
print('shape of transpose array',numpy.shape(trans_arr))

import numpy

arr=numpy.array([[1,2,3],[4,5,6]])
print(arr)
flatten=arr.flatten()
print(flatten)
'''
Task

You are given a
X integer array matrix with space separated elements ( = rows and

= columns).
Your task is to print the transpose and flatten results.

Input Format

The first line contains the space separated values of
and .
The next lines contains the space separated elements of

columns.

Output Format

First, print the transpose array and then print the flatten.

Sample Input

2 2
1 2
3 4

Sample Output

[[1 3]
 [2 4]]
[1 2 3 4]
'''

import numpy
n,m=tuple(map(int,input().split()))
arr=[input().split() for i in range(n)]
arr=numpy.array(arr)
print(numpy.transpose(arr))
print(arr.flatten())
