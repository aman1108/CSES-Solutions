from collections import defaultdict,deque
n,m=map(int,input().split())
G=defaultdict(list)
for i in range(m):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)
    
vis=[0 for i in range(n+1)]
Q=deque([1])
while(len(Q)!=0):
    a=Q.popleft()
    for b in G[a]:
        if (vis[b]==0):
            vis[b]=a
            Q.append(b)

if (vis[n]==0):
    print("IMPOSSIBLE")
else:
    ans=[n]
    val=n
    while(val!=1):
        val=vis[val]
        ans.append(val)
    ans.reverse()
    print(len(ans))
    print(*ans)
