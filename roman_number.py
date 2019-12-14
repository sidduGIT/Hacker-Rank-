'''
You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

Input Format

A single line of input containing a string of Roman characters.

Output Format

Output a single line containing True or False according to the instructions above.

Constraints

The number will be between
and

(both included).

Sample Input

CDXXI

Sample Output

True
'''

import re
str1=input()
m=re.match(r'[A-Za-z0-9]+',str1)
if m:
    print(True)
else:
    print(False)
