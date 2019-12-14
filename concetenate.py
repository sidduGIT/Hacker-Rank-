import numpy

arr_1=numpy.array([1,2,3])
arr_2=numpy.array([4,5,6])
arr_3=numpy.array([7,8,9])

print(arr_1,arr_2,arr_3)
print(numpy.concatenate((arr_1,arr_2,arr_3)))

import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])
print(numpy.concatenate((array_1,array_2),axis=1))
print(numpy.concatenate((array_1,array_2),axis=0))
