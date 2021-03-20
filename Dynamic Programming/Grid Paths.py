mod=(10**9)+7
n=int(input())
A=[]
for i in range(n):
    A.append(list(input()))

DP=[[0 for i in range(n)] for j in range(n)]
if (A[0][0]!='*'):
    DP[0][0]=1
for i in range(1,n):
    if (A[i][0]!='*'):
        DP[i][0]=DP[i-1][0]
    if (A[0][i]!='*'):
        DP[0][i]=DP[0][i-1]
    

for i in range(1,n):
    for j in range(1,n):
        if (A[i][j]!='*'):
            DP[i][j]=(DP[i][j]+DP[i-1][j]+DP[i][j-1])%mod

print(DP[n-1][n-1])
        
        
