'''
d=input();  #get rid of first line 
a=input().split();  #store all to array
s1=set();  #all unique room number
s2=set();  #all unique room number occur more than once
for i in a:
    if  i in s1:
        s2.add(i);
    else:
        s1.add(i);
s3=s1.difference(s2);
print(list(s3)[0]);

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print(pattern)
#print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

N, M = map(int,input().split())
for i in range(1,N,2):
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2):
    print((i * ".|.").center(M, "-"))
'''
for i in range(1,20):
    print(('*')*i)
print('SIDDU')
for i in range(20,1,-1):
    print(('*')*i)

