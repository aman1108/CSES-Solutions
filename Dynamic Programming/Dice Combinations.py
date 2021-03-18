mod=(10**9)+7
n=int(input())
DP=[0]*n
for i in range(n):
    if (i<6):
        DP[i]=2**i
    else:
        DP[i]=(DP[i-1]+DP[i-2]+DP[i-3]+DP[i-4]+DP[i-5]+DP[i-6])%mod
print(DP[n-1])
