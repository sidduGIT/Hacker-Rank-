
from collections import Counter
str1='aabbbccde'
x=sorted(str1)
print(x)
print(Counter(x))
c=Counter(x).most_common(3)
print(c)
for k,v in c:
    print(k,v)

