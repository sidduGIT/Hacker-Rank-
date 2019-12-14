'''
Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, given the number , its reverse is . Their difference is . The number reversed is , and their difference is

.

She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.

Given a range of numbered days,
and a number , determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where is evenly divisible by

. If a day's value is a beautiful number, it is a beautiful day. Print the number of beautiful days in the range.

Function Description

Complete the beautifulDays function in the editor below. It must return the number of beautiful days in the range.

beautifulDays has the following parameter(s):

    i: the starting day number
    j: the ending day number
    k: the divisor

Input Format

A single line of three space-separated integers describing the respective values of
, , and

.

Constraints

Output Format

Print the number of beautiful days in the inclusive range between
and

.

Sample Input

20 23 6

Sample Output

2

Explanation

Lily may go to the movies on days
, , , and

. We perform the following calculations to determine which days are beautiful:

    Day

is beautiful because the following evaluates to a whole number: Day is not beautiful because the following doesn't evaluate to a whole number: Day is beautiful because the following evaluates to a whole number: Day is not beautiful because the following doesn't evaluate to a whole number: Only two days, and , in this interval are beautiful. Thus, we print as our answer.
'''
def reversed1(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
#print(reversed1(int('1234')))

def beautiful_day(i,j,k):
    count=0
    for n in range(i,j+1):
        if (abs(n-reversed1(n))%k)==0:
            count+=1
    return count
ijk=input().split()
i=int(ijk[0])
j=int(ijk[1])
k=int(ijk[2])
print(beautiful_day(i,j,k))

