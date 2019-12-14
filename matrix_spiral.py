'''
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
'''

matrix=[[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]
result1=[]
result2=[]
inner_result1=[]
inner_result2=[]
for i in range(4):
    if i%2==0:
        for j in range(5):
            inner_result1.append(matrix[i][j])
        result1.append(inner_result1)
    else:
        for j in range(5):
            inner_result2.append(matrix[i][j])
#result1.append(inner_result1)
        result1.append(inner_result2[::-1])
print(result1)

