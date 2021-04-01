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
A=[]
for i in range(m):
    A.append(list(map(int,input().split())))


A.sort(key=lambda x:x[2] )
par=[i for i in range(n+1)]
rank=[0]* (n+1)
ans=0
cnt=0
for a,b,c in A:
    x=find(a)
    y=find(b)
    if (x!=y):
        ans=ans+c
        cnt=cnt+1
        union(x,y)

 
if (cnt!=n-1):
    print("IMPOSSIBLE")
else:
    print(ans)
