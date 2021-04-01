import sys
input=sys.stdin.readline
def find(i):
    while(par[i]!=i):
        i=par[i]
    return i

def union(x,y):
    if (rank[x]<rank[y]):
        par[x]=y
    elif (rank[y]>rank[x]):
        par[y]=x
    else:
        par[y]=x
        rank[x]+=1
        
n,m=map(int,input().split())
par=[i for i in range(n+1)]
rank=[1]* (n+1)
node=[1]* (n+1)
ans=1
cnt=n
for i in range(m):
    a,b=map(int,input().split())
    x=find(a)
    y=find(b)
    if (x!=y):
        union(x,y)
        cnt=cnt-1
        node[x]=node[x]+node[y]
        node[y]=node[x]
        ans=max(ans,node[x])
        print(cnt,ans)

    else:
        print(cnt,ans)
 
