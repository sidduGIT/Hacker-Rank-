'''
ABCXYZ company has up to

employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

    It must contain at least

uppercase English alphabet characters.
It must contain at least
digits ( -
).
It should only contain alphanumeric characters (
- , - & -
).
No character should repeat.
There must be exactly

    characters in a valid UID.

Input Format

The first line contains an integer
, the number of test cases.
The next

lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354

Sample Output

Invalid
Valid

Explanation

B1CD102354:
is repeating → Invalid
B1CDEF2354: Valid
'''
import re
#str1='B1CDEF2354'
for _ in range(int(input())):
    str1=input()
    str1=''.join(sorted(str1))
    upper=bool(re.search(r'[A-Z]{2,}',str1))
    digits=bool(re.search(r'[0-9]{3,}',str1))
    alphanumeric=bool(re.search(r'[a-zA-Z0-9]{10}$',str1))
    repeat=not bool(re.search(r'(.)\1',str1))
    if (upper and digits and alphanumeric and repeat):
        print('Valid')
    else:
        print('Invalid')
