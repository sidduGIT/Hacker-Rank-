'''
You are given a function . You are also given lists. The list consists of

elements.

You have to pick one element from each list so that the value from the equation below is maximized:

% denotes the element picked from the list . Find the maximized value

obtained.

denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains
space separated integers and .
The next lines each contains an integer , denoting the number of elements in the list, followed by

space separated integers denoting the elements in the list.

Constraints




Output Format

Output a single integer denoting the value

.

Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

Sample Output

206

Explanation

Picking 5 from the st list, 9 from the nd list and 10 from the rd list gives the maximum value equal to % = 5**2+9**2+10**2.
'''
from itertools import product

lst1=[1,2,3]
lst2=[4,5,6]
lst3=[7,8,9]
print(list(product(lst1,lst2,lst3)))

#print(list(zip(lst1,lst2,lst3)))

K,M=map(int,input().split())
lst=(list(map(int,input().split()))[1:] for _ in range(K))
results=map(lambda x:sum(i**2 for i in x)%M,product(*lst))
print(max(results))

