import sys
input=sys.stdin.readline

from collections import defaultdict

n,m=map(int,input().split())
G=defaultdict(list)

vis=[0 for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    G[a].append(b)
    vis[b]+=1

Q=[]
for i in range(1,n+1):
    if (vis[i]==0):
        Q.append(i)

ans=[]
while(len(Q)!=0):
    a=Q.pop()
    ans.append(a)
    for i in G[a]:
        vis[i]=vis[i]-1
        if (vis[i]==0):
            Q.append(i)
        
if (len(ans)!=n):
    print("IMPOSSIBLE")

else:
    print(*ans)
