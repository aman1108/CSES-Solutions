n,x=map(int,input().split())
A=list(map(int,input().split()))
DP=[10**9]*(x+1)
DP[0]=0
for v in A:
    for i in range(x-v+1):
        DP[i+v]=min(DP[i+v],DP[i]+1)
        
if (DP[x]==10**9):
    print(-1)
else:
    print(DP[x])
            
