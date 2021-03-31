import sys
input=sys.stdin.readline

from collections import defaultdict

n,m=map(int,input().split())
G=defaultdict(list)

vis=[0 for i in range(n+1)]
val=[(-1*(10**9)) for i in range(n+1)]
par=[0 for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    G[a].append(b)
    vis[b]+=1

Q=[]
for i in range(1,n+1):
    if (vis[i]==0):
        Q.append(i)

val[1]=1
ans=[]
while(len(Q)!=0):
    a=Q.pop()
    ans.append(a)
    for i in G[a]:
        vis[i]=vis[i]-1
        if (vis[i]==0):
            Q.append(i)
        if (val[i]<(val[a]+1)):
            val[i]=val[a]+1
            par[i]=a

if (val[n]<0):
    print("IMPOSSIBLE")

else:
    ans=[]
    val=n
    while(val!=0):
        ans.append(val)
        val=par[val]
    ans.reverse()
    print(len(ans))
    print(*ans)
    
    
    
            

