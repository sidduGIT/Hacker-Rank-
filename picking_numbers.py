lst=[1,2,2,3,1,2]
lst=[int(i) for i in lst]
maximum=0
set1=set(lst)
for i in set1:
    first=lst.count(i)
    second=lst.count(i-1)
    if first+second>maximum:
        maximum=first+second
print(maximum)


