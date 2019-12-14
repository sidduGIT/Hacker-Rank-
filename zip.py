print(list(zip([1,2,3,4,5,6],'hacker')))

print(list(zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])))

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]
print(X)
print(list(zip(*X)))
'''
Task

The National University conducts an examination of
students in

subjects.
Your task is to compute the average scores of each student.

The format for the general mark sheet is:

Student ID → ___1_____2_____3_____4_____5__
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5

Input Format

The first line contains
and separated by a space.
The next

lines contains the space separated marks obtained by students in a particular subject.

Constraints


Output Format

Print the averages of all students on separate lines.

The averages must be correct up to

decimal place.

Sample Input

5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5

Sample Output

90.0
91.0
82.0
90.0
85.5
'''
marks=[]
n,x=map(int,input().split())
for i in range(x):
    marks.append(list(map(float,input().split())))
for i in range(n):
    sum1=0
    avg=0
    for j in range(x):
        sum1=sum1+marks[j][i]
    avg=sum1/x
    print(avg)

print(marks)
for mark in (zip(*marks)):
    print(sum(mark)/len(mark))

