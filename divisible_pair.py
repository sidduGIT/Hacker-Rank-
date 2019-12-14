'''
You are given an array of integers, , and a positive integer, . Find and print the number of pairs where and + is divisible by

.

For example,
and . Our three pairs meeting the criteria are and

.

Function Description

Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.

divisibleSumPairs has the following parameter(s):

    n: the integer length of array

    ar: an array of integers
    k: the integer to divide the pair sum by

Input Format

The first line contains
space-separated integers, and .
The second line contains space-separated integers describing the values of

.

Constraints

Output Format

Print the number of
pairs where and + is evenly divisible by

.

Sample Input

6 3
1 3 2 6 1 2

Sample Output

 5

Explanation

Here are the
valid pairs when

:
'''
from itertools import combinations
n=int(input())
ar=list(map(int,input().split()))
k=int(input())

def divisibleSumPairs(n, k, ar):
    '''sum_lst = list()
    res = list()
    comb_list = (list(combinations(ar, 2)))
    for i in comb_list:
        sum_lst.append(i[0] + i[1])
    for i in sum_lst:
        if (i % k) == 0:
            res.append(i)
    return (len(res))
    '''
    count=0
    for i in range(n-1):
        j=i+1
        while j<n:
            if ((ar[i]+ar[j])%k==0):
                count+=1
            j+=1
    return count
print(divisibleSumPairs(n, k, ar))

'''
for i in combinations(ar,2):
    if i[0]<i[1]:
        if (sum(i)%k==0):
            print(i)
'''
