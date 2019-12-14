'''
A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, he decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time () to arrived late (

).

Given the arrival time of each student and a threshhold number of attendees, determine if the class is canceled.

Input Format

The first line of input contains

, the number of test cases.

Each test case consists of two lines.

The first line has two space-separated integers,
and , the number of students (size of ) and the cancellation threshold.
The second line contains space-separated integers (

) describing the arrival times for each student.

Note: Non-positive arrival times (
) indicate the student arrived early or on time; positive arrival times () indicate the student arrived

minutes late.

For example, there are
students who arrive at times . Four are there on time, and two arrive late. If there must be for class to go on, in this case the class will continue. If there must be

, then class is cancelled.

Function Description

Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.

angryProfessor has the following parameter(s):

    k: the threshold number of students
    a: an array of integers representing arrival times

Constraints

Output Format

For each test case, print the word YES if the class is canceled or NO if it is not.

Note
If a student arrives exactly on time

, the student is considered to have entered before the class started.

Sample Input

2
4 3
-1 -3 4 2
4 2
0 -1 2 1

Sample Output

YES
NO

Explanation

For the first test case,
. The professor wants at least students in attendance, but only have arrived on time ( and

) so the class is cancelled.

For the second test case,
. The professor wants at least students in attendance, and there are who have arrived on time ( and

) so the class is not cancelled.
Python 3
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
'''

def class_status(students,k):
    arrival=[i for i in students if i<0 or i==0]
    if len(arrival)<k:
        return ('YES')
    else:
        return ('NO')

for _ in range(int(input())):
    nk=input().split()
    n=int(nk[0])
    k=int(nk[1])
    students=list(map(int,input().split()))
    print(class_status(students,k))
