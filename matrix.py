'''
Neo has a complex matrix script. The matrix script is a X

grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

[Capture.JPG]

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers
(rows) and (columns) respectively.
The next

lines contain the row elements of the matrix script.

Constraints

Note: A

score will be awarded for using 'if' conditions in your code.

Output Format

Print the decoded matrix script.

Sample Input 0

7 3
Tsi
h%x
i #
sM
$a
#t%
ir!

Sample Output 0

This is Matrix#  %!

Explanation 0

The decoded script is:

This$#is% Matrix#  %!

Neo replaces the symbols or spaces between two alphanumeric characters with a single space   ' ' for better readability.

So, the final decoded script is:

This is Matrix#  %!
'''

mat=[[1,2,3],[4,5,6],[7,8,9]]
cmat=[]
for i in range(len(mat)):
    inner=[]
    for j in range(len(mat)):
        #print(mat[j][i])
        inner.append(mat[j][i])
    cmat.append(inner)
print(cmat)
'''
import re
row_col=input().split()
row=int(row_col[0])
col=int(row_col[1])
print(row,col)
matrix=[]
for _ in range(row):
    matrix_item=input()
    matrix.append(matrix_item)
print(matrix)

matrix=[['Tsi'], ['h%x'], ['i #'], ['sM '], ['$a '], ['#t%'], ['ir!']]
for i in range(7):
    for j in range(3):
        print(matrix[i][j])
'''
'''
import re
n,m = map(int,input().split())
matrix = []
s = ''
for line in range(n):
    matrix.append(input())
s = ''.join(matrix[i][j] for j in range(m) for i in range(n))
s1 = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])',' ',s)
print(s1)
'''
import re

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))

