'''
Given the time in numerals we may convert it into words, as shown below:

At
, use o' clock. For , use past, and for

use to. Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described.

Function Description

Complete the timeInWords function in the editor below. It should return a time string as described.

timeInWords has the following parameter(s):

    h: an integer representing hour of the day
    m: an integer representing minutes after the hour

Input Format

The first line contains
, the hours portion The second line contains

, the minutes portion

Constraints

Output Format

Print the time in words as described.

Sample Input 0

5
47

Sample Output 0

thirteen minutes to six

Sample Input 1

3
00

Sample Output 1

three o' clock

Sample Input 2

7
15

Sample Output 2

quarter past seven

'''
def time_in_words(h,m):
    result=[]
    ByOne=[0,'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve',
       'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen','twenty']
    ByQua=["%s o' clock", "quarter past %s", "half past %s", "quarter to %s"]
    for i in range(1,10):
        ByOne.append('twenty %s'%ByOne[i])

    hour=ByOne[h] if (m<31) else ByOne[h+1]
    if m==1 and hour==1:
        result.append("%s minute"%ByOne[m]+"s"*(m==1)+ " past %s"%hour)
    elif not m%15:
        #print(ByQua[m//15] % hour)
        result.append(ByQua[m//15] % hour)
    elif m<30:
        result.append("%s minute"%ByOne[m]+"s"*(m==1)+ " past %s"%hour)
    else:
        result.append("%s minute"%ByOne[60-m]+"s"*(m==59)+ " to %s"%hour)
    for i in result:
        return (i)

h=int(input())
m=int(input())
print(time_in_words(h,m))
