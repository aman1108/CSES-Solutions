import sys
input=sys.stdin.readline

from collections import defaultdict

mod=(10**9)+7
n,m=map(int,input().split())
G=defaultdict(list)

vis=[0 for i in range(n+1)]
ans=[0 for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    G[a].append(b)
    vis[b]+=1

ans[1]=1
Q=[]
for i in range(1,n+1):
    if (vis[i]==0):
        Q.append(i)


while(len(Q)!=0):
    a=Q.pop()
    for i in G[a]:
        vis[i]=vis[i]-1
        ans[i]=(ans[i]+ans[a])%mod
        if (vis[i]==0):
            Q.append(i)

#print(ans)
print(ans[n])
