mod=(10**9)+7
n,x=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
DP=[0 for i in range(x+1)]
DP[0]=1
for i in range(x):
    for j in range(n):
        if (i+A[j]<=x):
            DP[i+A[j]]=(DP[i+A[j]]+DP[i])%mod
        else:
            break

print(DP[x])
        
