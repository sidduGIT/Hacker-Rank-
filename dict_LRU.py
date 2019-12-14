'''
This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.
    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
'''

dict1={}

def set_item(key,value):
    dict1[key]=value
    return dict1

def get_item(key):
    if key in dict1:
        return dict1[key]
    else:
        return 'item not listed'

set_item('A',1)
set_item('B',2)
set_item('C',3)
set_item('D',4)
print(dict1)

for i in ('A','C','Z'):
    print(get_item(i))
#get_item('A')
#get_item('C')
#get_item('Z')

