'''n=int(input())
student_marks={}
for i in range(n):
    line=input().split()
    name,scores=line[0],line[1:]
    scores=list(map(float,scores))
    student_marks[name]=scores
query_name=input()
print(student_marks)

if query_name in student_marks:
    print(sum(student_marks[query_name])/len(student_marks[query_name]))

You are given a string .
contains alphanumeric characters only.
Your task is to sort the string

in the following manner:

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

Input Format

A single line of input contains the string

.

Constraints

Output Format

Output the sorted string

.

Sample Input

Sorting1234

Sample Output

ginortS1324

str1=input()
lower=[i for i in str1 if i.islower()]
upper=[i for i in str1 if i.isupper()]
even=[i for i in str1 if i.isdigit() and int(i)%2==0]
odd=[i for i in str1 if i.isdigit() and int(i)%2!=0]
print(''.join(sorted(lower)+sorted(upper)+sorted(odd)+sorted(even)))
'''

'''
A valid email address meets the following criteria:

    It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
    The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
    The domain and extension contain only English alphabetical characters.
    The extension is

, , or

    characters in length.

Given

pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

Hint: Try using Email.utils() to complete this challenge. For example, this code:

import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))

produces this output:

('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>

Input Format

The first line contains a single integer,
, denoting the number of email address.
Each line of the

subsequent lines contains a name and an email address as two space-separated values following this format:

name <user@email.com>

Constraints

Output Format

Print the space-separated name and email address pairs containing valid email addresses only. Each pair must be printed on a new line in the following format:

name <user@email.com>

You must print each valid email address in the same order as it was received as input.

Sample Input

2
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

Sample Output

DEXTER <dexter@hotmail.com>

Explanation

dexter@hotmail.com is a valid email address, so we print the name and email address pair received as input on a new line.
virus!@variable.:p is not a valid email address because the username contains an exclamation point (!) and the extension contains a colon (:). As this email is not valid, we print nothing.

import re
n=int(input())
for i in range(n):
    name,ip=input().split()
    valid_ip=re.findall(r'<[A-Za-z0-9-._]+@[A-Za-z]+.[A-Za-z]{1,3}>',ip)
    if valid_ip:
        print(name,valid_ip[0])
'''

'''
students=[]
for _ in range(int(input())):
    record=[]
    name=input()
    record.append(name)
    score=float(input())
    record.append(score)
    students.append(record)

#print(sorted(students,key=lambda x:x[1]))
second=sorted(list(set([score for name,score in students])))[1]
print(second)
print('\n'.join([a for a,b in sorted(students) if b==second]))

students=[]
for _ in range(int(input())):
    name=input()
    score=float(input())
    students.append([name,score])

#print(sorted(students,key=lambda x:x[1]))
second=sorted(list(set([score for name,score in students])))[1]
print(second)
print('\n'.join([a for a,b in sorted(students) if b==second]))
'''

#transpose

import numpy
my_array=numpy.array([[1,2,3],[4,5,6]])
print(my_array.transpose())

#flatten

import numpy
my_array=numpy.array([[1,2,3],[4,5,6]])
print(my_array.flatten())

'''
Task

Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

Constraints

Output Format

Output total number of students who have subscriptions to the English or the French newspaper but not both.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

8

Explanation

The roll numbers of students who have subscriptions to English or French newspapers but not both are:
and .
Hence, the total is students.

ne=int(input())
e=input().split()
e=list(map(int,e))
nf=int(input())
f=input().split()
f=list(map(int,f))
print(len(set(e).symmetric_difference(set(f))))
'''
'''
You are given a string .
Your task is to find the first occurrence of an alphanumeric character in

(read from left to right) that has consecutive repetitions.

Input Format

A single line of input containing the string

.

Constraints

Output Format

Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

Sample Input

..12345678910111213141516171820212223

Sample Output

1

Explanation

.. is the first repeating character, but it is not alphanumeric.
1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.

import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
#print(m.groups())
print(m.group(1) if m else -1)

import re
str1=input()
m=re.findall(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}[AEIOUaeiou]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}',str1)

print(m)
if m:
    for i in m:
        print(i[1:-1])
else:
    print(-1)
'''

'''
Task
Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter. The constructor must assign to after confirming the argument passed as is not negative; if a negative argument is passed as , the constructor should set to

and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:

    yearPasses() should increase the

instance variable by
.
amIOld() should perform the following conditional actions:

    If

, print You are young..
If
and

        , print You are a teenager..
        Otherwise, print You are old..

To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!

Note: Do not remove or alter the stub code in the editor.

Input Format

Input is handled for you by the stub code in the editor.

The first line contains an integer,
(the number of test cases), and the subsequent lines each contain an integer denoting the

of a Person instance.

Constraints

Output Format

Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print
or lines (depending on whether or not a valid

was passed to the constructor).

Sample Input

4
-1
10
16
18

Sample Output

Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.


class Person:

    def __init__(self,initialAge):
        self.age=0
        if initialAge<0:
            print('Age is not valid, setting age to 0')
        else:
            self.age=initialAge

    def yearPasses(self):
        global age
        age=age+1

    def amIOld(self):
        if age<13:
            print('You are young')
        elif age>=13 and age<18:
            print('You are a teenager')
        elif age>=18:
            print('You are old')

for i in range(0,int(input())):
    age=int(input())
    p=Person(age)
    p.amIOld()
    for j in range(0,3):
        p.yearPasses()
    p.amIOld()
    print('')
'''
'''
You are given a string .
Your task is to verify that

is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

Number can start with +, - or . symbol.
For example:
✔+4.50
✔-1.0
✔.5
✔-.7
✔+.4
✖ -+4.5

Number must contain at least

decimal value.
For example:
✖ 12.
✔12.0

Number must have exactly one . symbol.
Number must not give any exceptions when converted using

.

Input Format

The first line contains an integer
, the number of test cases.
The next line(s) contains a string

.

Constraints

Output Format

Output True or False for each test case.

Sample Input 0

4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output 0

False
True
True
False
'''

import re
for i in range(int(input())):
    N=input()
    m=re.search(r'^[+-]?[0-9]*\.[0-9]+$',N)
    if (m):
        print(True)
    else:
        print(False)



