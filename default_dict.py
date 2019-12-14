'''
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
For example:

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i

This prints:

('python', ['awesome', 'language'])
('something-else', ['not relevant'])

In this challenge, you will be given
integers, and . There are words, which might repeat, in word group . There are words belonging to word group . For each words, check whether the word has appeared in group or not. Print the indices of each occurrence of in group . If it does not appear, print

.

Constraints


Input Format

The first line contains integers,
and separated by a space.
The next lines contains the words belonging to group .
The next lines contains the words belonging to group

.

Output Format

Output
lines.
The line should contain the -indexed positions of the occurrences of the

word separated by spaces.

Sample Input

5 2
a
a
b
a
b
a
b

Sample Output

1 2 4
3 5

Explanation

'a' appeared
times in positions , and .
'b' appeared times in positions and .
In the sample problem, if 'c' also appeared in word group , you would print .
'''

from collections import defaultdict

d=defaultdict(list)

d['bagewadi'].append('atharv')
d['mogali'].append('suraj')
d['bagewadi'].append('surabhi')
d['mogali'].append('suman')
print(d)

for i in d.items():
    print(i)

dict1={'A':1}
dict2=defaultdict(int)
if 'A' in dict1:
    print(dict1['A'])

#if 'A' in dict2:
print(dict2)

n,m=map(int,input().split())
dA=defaultdict(list)
listB=[]
for i in range(n):
    dA[input()].append(i+1)

print(dA)

for i in range(m):
    listB=listB+[input()]

print(listB)
for i in listB:
    if i in dA:
        print(' '.join(map(str,dA[i])))
    else:
        print('-1')

