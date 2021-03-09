n,x=map(int,input().split())
A=list(map(int,input().split()))
vis=[0 for i in range(n)]
A.sort()
j=n-1
ans=0
for i in range(n):
    if (vis[i]==0):
        ans=ans+1
        vis[i]=1
        while (j>0):
            if (vis[j]==0 and A[i]+A[j]<=x):
                vis[j]=1
                break
            j=j-1
print(ans)
