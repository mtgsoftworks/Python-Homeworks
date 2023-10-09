A = [ [0,1] , [1,0]]
B = [[2,1],[1,0]]
C = [[0,0],[0,0]]

for i in range(2):
     for j in range(2):
          C[i][j] = A[i][j] * B[j][i]

print(str(C))
