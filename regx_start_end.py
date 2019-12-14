'''
start() & end()

These expressions return the indices of the start and end of the substring matched by the group.

Code

>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0

Task
You are given a string
.
Your task is to find the indices of the start and end of string in

.

Input Format

The first line contains the string
.
The second line contains the string

.

Constraints


Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input

aaadaa
aa

Sample Output

(0, 1)
(1, 2)
(4, 5)
'''

import re
m=re.search(r'\d+','1234')
print(m.start())
print(m.end())

s=input()
k=input()
pattern=re.compile(k)
m=pattern.search(s)

if not m:
    print('(-1,-1)')
while m:
    print('({0},{1})'.format(m.start(),m.end()-1))
    m=pattern.search(s,m.start()+1)
