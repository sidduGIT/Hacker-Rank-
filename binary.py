'''
Objective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base-
integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in

's binary representation.

Input Format

A single integer,

.

Constraints

Output Format

Print a single base-
integer denoting the maximum number of consecutive 's in the binary representation of

.

Sample Input 1

5

Sample Output 1

1

Sample Input 2

13

Sample Output 2

2

Explanation

Sample Case 1:
The binary representation of
is , so the maximum number of consecutive 's is

.

Sample Case 2:
The binary representation of
is , so the maximum number of consecutive 's is .
'''
n=int(input())
print(bin(n))
nbin=str(bin(n))
nbin=nbin.replace('0b','')
print(max([len(i) for i in nbin.split('0')]))
#print([len(i) for i in nbin.split('0')])

n=int(input())
print(max(len(i) for i in bin(n)[2:].split('0')))

#for checking consecutive '0'

n=int(input())
print(max(len(i) for i in bin(n)[2:].split('1')))
print([len(i) for i in bin(n)[2:].split('1')])
