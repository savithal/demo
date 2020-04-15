A = [[5,6],[1,2]]
B = [[5,6],[1,2]]
#B = [[1,2,3],[3,4,1]]
from numpy import *;
#m= matrix('1,2,3;4,6,4;1,2,2')
#n = matrix('1,2;6,2;2,4')
#print(m*n)
print("A's matrix size=",len(A),"*",len(A[0]))
print("B's matrix=",len(B),"*",len(B[0]))
if (len(A[0])== (len(B))):
    print("Matrix multiplication possible")
else:
    print("Invalid row and col,cant multiply matrix")
    exit(1)

result = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[k][j]*B[j][k]
print(result)


