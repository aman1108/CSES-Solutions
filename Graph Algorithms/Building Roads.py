from collections import defaultdict
n,m=map(int,input().split())
G=defaultdict(list)
for i in range(m):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)

vis=[0 for i in range(n+1)]
lnode=1
ans=[]
for i in range(1,n+1):
    if (vis[i]==0):
        Q=[i]
        while(len(Q)!=0):
            a=Q.pop()
            vis[a]=1
            for b in G[a]:
                if (vis[b]==0):
                    Q.append(b)
                    vis[b]=1

        if (i!=1):
            ans.append([lnode,i])
print(len(ans))
for val in ans:
    print(*val)
