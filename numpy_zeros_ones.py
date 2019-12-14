import numpy
print(numpy.zeros((1,2))) #default is float
print(numpy.zeros((3,2)))

print(numpy.zeros((3,2),dtype=numpy.int))

print(numpy.ones((3,2)))
print(numpy.ones((3,2),dtype=numpy.int))

'''
Task

You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Input Format

A single line containing the space-separated integers.

Constraints

Output Format

First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.

Sample Input 0

3 3 3

Sample Output 0

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]

Explanation 0

Print the array built using numpy.zeros and numpy.ones tools and you get the result as shown.
'''
import numpy
nums=tuple(map(int,input().split()))
print(numpy.zeros(nums,dtype=numpy.int))
print(numpy.ones(nums,dtype=numpy.int))

