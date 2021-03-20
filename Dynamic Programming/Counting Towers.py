mod=(10**9)+7
mv=10**6
DP1=[0 for i in range(mv)]
DP2=[0 for i in range(mv)]
DP1[0]=1
DP2[0]=1
for i in range(1,mv):
    DP1[i]=(DP1[i]+((DP1[i-1]*2)%mod)+DP2[i-1])%mod
    DP2[i]=(DP2[i]+((DP2[i-1]*4)%mod)+DP1[i-1])%mod



T=int(input())
for _ in range(T):
    n=int(input())
    print((DP1[n-1]+DP2[n-1])%mod)
        
