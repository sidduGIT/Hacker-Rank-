'''
collections.deque()

A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same

performance in either direction.

Click on the link to learn more about deque() methods.
Click on the link to learn more about various approaches to working with deques: Deque Recipes.
'''

from collections import deque

d=deque()
d.append(1)
print(d)

d.appendleft(2)
print(d)

d.extend('3')
print(d)

d.extendleft('456')
print(d)

print(d.count(1))

print(d.pop())
print(d)

print(d.popleft())
print(d)

d.extend('78910')
print(d)

d.remove('5')
print(d)

d.reverse()
print(d)

d.rotate(3)
print(d)
'''
Task

Perform append, pop, popleft and appendleft methods on an empty deque

.

Input Format

The first line contains an integer
, the number of operations.
The next

lines contains the space separated names of methods and their values.

Constraints

Output Format

Print the space separated elements of deque

.

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output

1 2

d=deque()
n=int(input())
for i in range(n):
    operation,num=input().split()
    if operation=='append':
        d.append(num)
    elif operation=='appendleft':
        d.appendleft(num)
    elif operation=='pop':
        d.pop()
    elif operation=='popleft':
        d.popleft()
for i in d:
    print(i,end=' ')
'''
d.clear()
from collections import deque

for _ in range(int(input())):
    operation,*args=input().split()
    getattr(d,operation)(*args)
print(*d)


