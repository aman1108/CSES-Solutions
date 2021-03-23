from collections import defaultdict,deque
n,m=map(int,input().split())
G=defaultdict(list)
for i in range(m):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)
    
vis=[0 for i in range(n+1)]
flag=0
for i in range(1,n+1):
    if (vis[i]==0):
        Q=[i]
        vis[i]=1
        cnt=0
        while(len(Q)!=0):
            a=Q.pop()
            cnt=(vis[a]%2)+1
            for b in G[a]:
                if (vis[b]==0):
                    vis[b]=cnt
                    Q.append(b)
                elif (vis[b]==vis[a]):
                    #print(b,a,vis[b],vis[a])
                    flag=1
                    break
            if (flag==1):
                break
    if (flag==1):
        break

if (flag==1):
    print("IMPOSSIBLE")

else:
    print(*vis[1:])
