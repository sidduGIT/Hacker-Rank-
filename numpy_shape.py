import numpy

arr_1D=numpy.array([1,2,3,4,5,6])
print(arr_1D.shape)

arr_2D=numpy.array([[1,2],[3,4],[5,6]])
print(arr_2D.shape)

change_arr=numpy.array([1,2,3,4,5,6])
change_arr.shape=(3,2)
print(change_arr)

arr_1D=numpy.array([1,2,3,4,5,6])
print(numpy.reshape(arr_1D,(3,2)))
print(numpy.reshape(arr_1D,(2,3)))
print(numpy.reshape(arr_1D,(1,6)))
print(numpy.reshape(arr_1D,(6,1)))
'''
Task

You are given a space separated list of nine integers. Your task is to convert this list into a
X

NumPy array.

Input Format

A single line of input containing

space separated integers.

Output Format

Print the
X
hape
NumPy array.

Sample Input

1 2 3 4 5 6 7 8 9

Sample Output

[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

arr=numpy.array(input().split(),int)
print(numpy.reshape(arr,(3,3)))
