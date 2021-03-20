n=int(input())
DP=[10**9 for i in range(n+1)]
for i in range(1,min(10,n+1)):
    DP[i]=1

for i in range(10,n+1):
    v=str(i)
    for j in v:
        DP[i]=min(1+DP[i-int(j)],DP[i])
print(DP[n])
