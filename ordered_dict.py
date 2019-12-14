'''
collections.OrderedDict

An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

Example

Code

>>> from collections import OrderedDict
>>>
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>>
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>>
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>>
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

Task

You are the manager of a supermarket.
You have a list of

items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items,
.
The next

lines contains the item's name and price, separated by a space.

Constraints

Output Format

Print the item_name and net_price in order of its first occurrence.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

Explanation

BANANA FRIES: Quantity bought:
, Price:
Net Price:
POTATO CHIPS: Quantity bought: , Price:
Net Price:
APPLE JUICE: Quantity bought: , Price:
Net Price:
CANDY: Quantity bought: , Price:
Net Price:
'''
from collections import OrderedDict

ordinary_dict={}
ordinary_dict['a']=1
ordinary_dict['b']=2
ordinary_dict['c']=3
ordinary_dict['d']=4
ordinary_dict['e']=5

print(ordinary_dict)

ordered_dict=OrderedDict()
ordered_dict['e']=5
ordered_dict['d']=4
ordered_dict['c']=3
ordered_dict['b']=2
ordered_dict['a']=1
print(dict(ordered_dict))
'''
str1='BANANA FRIES 12'
words=str1.split()
print(' '.join(words[0:2]))
print(words[2:])
'''
from collections import OrderedDict
'''
items=OrderedDict()
for _ in range(int(input())):
    item_price=input().split()
    items[' '.join(item_price[0:2])]=int(item_price[-1])
for item_name,price in items.items():
    print(item_name,price)
'''
from collections import OrderedDict
dict1=OrderedDict()
for _ in range(int(input())):
    item,space,price=input().rpartition(' ')
    dict1[item]=dict1.get(item,0)+int(price)
for item_name,price in dict1.items():
    print(item_name,price)




