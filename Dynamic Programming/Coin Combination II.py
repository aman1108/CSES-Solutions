mod=(10**9)+7
n,x=map(int,input().split())
A=list(map(int,input().split()))
DP=[0 for i in range(x+1)]
DP[0]=1
for i in range(n):
    for j in range(x-A[i]+1):
        DP[j+A[i]]=(DP[j+A[i]]+DP[j])%mod
print(DP[x])
        
