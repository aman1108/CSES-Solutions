mod=(10**9)+7
n,m=map(int,input().split())
A=list(map(int,input().split()))

DP=[[0 for i in range(m+2)] for i in range(n)]
if (A[0]==0):
    for i in range(1,m+1):
        DP[0][i]=1
else:
    DP[0][A[0]]=1
    
for i in range(1,n):
    v=A[i]
    if (v==0):
        for j in range(1,m+1):
            DP[i][j]=(DP[i][j]+DP[i-1][j]+DP[i-1][j-1]+DP[i-1][j+1])%mod
    else:
        DP[i][v]=(DP[i][v]+DP[i-1][v]+DP[i-1][v-1]+DP[i-1][v+1])%mod

ans=0
for i in DP[n-1]:
    ans=(ans+i)%mod
print(ans)
