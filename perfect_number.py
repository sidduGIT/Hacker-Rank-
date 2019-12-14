'''
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''
n=int(input())
k=int(input())
perfect=[]
if n>10 and n<=100:
    print('perfect numbers are')
    for i in range(10,n+1):
        i=str(i)
        if (int(i[0])+int(i[1])==10):
            #print(i)
            perfect.append(i)
            
    print(perfect[k-1])
else:
    print('invalid number')

