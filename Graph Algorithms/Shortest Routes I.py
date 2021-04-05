import sys
input=sys.stdin.readline
import heapq

n,m=map(int,input().split())
vis=[-1]* (n+1)
dis=[float("inf")]*(n+1)
Q=[[0,1]]
heapq.heapify(Q)

G=[[] for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    G[a].append([b,c])

while(len(Q)!=0):
    v,c=heapq.heappop(Q)
    if (vis[c]==-1):
        vis[c]=v
        dis[c]=v
        for c1,v1 in G[c]:
            if (vis[c1]==-1 and v1+v<dis[c1]):
                heapq.heappush(Q,[v1+v,c1])
                dis[c1]=v1+v
print(*vis[1:])
    

