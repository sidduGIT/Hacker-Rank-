'''
Task

The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

Input Format

The first line contains an integer,
, the number of students who have subscribed to the English newspaper.
The second line contains space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains

space separated roll numbers of those students.

Constraints

Output Format

Output the total number of students who have at least one subscription.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

13

Explanation

Roll numbers of students who have at least one subscription:
and . Roll numbers: and are in both sets so they are only counted once.
Hence, the total is students.
'''
ne=int(input())
re=list(map(int,input().split()))
nf=int(input())
rf=list(map(int,input().split()))
print(len(set(re).union(set(rf))))

