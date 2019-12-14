'''
This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
'''

import random
while(True):
    def rand7(n):
        return (random.choice([i for i in range(1,n+1)]))
    print('random number from 1 to 7')
    print(rand7(7))

    def rand5(n):
        return (random.choice([i for i in range(1,n+1)]))

    print('random number from 1 to 5')
    print(rand5(5))

