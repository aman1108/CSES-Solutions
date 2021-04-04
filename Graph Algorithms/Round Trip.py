from collections import defaultdict,deque
n,m=map(int,input().split())

G=defaultdict(list)
for i in range(m):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)
    
vis=[0 for i in range(n+1)]
par=[0 for i in range(n+1)]
flag=0
ans=[]
st,end=0,0
for i in range(1,n+1):
    if (vis[i]==0):
        Q=[i]
        while(len(Q)!=0):
            a=Q.pop()
            vis[a]=1
            for b in G[a]:
                if (vis[b]==0):
                    vis[b]=1
                    par[b]=a
                    Q.append(b)

                elif (par[a]!=b):
                    flag=1
                    st=par[b]
                    end=b
                    par[b]=a
                    break
            if(flag==1):
                break
    if(flag==1):
        break

if(flag==0):
    print("IMPOSSIBLE")

else:
    ans=[end]
    end1=end
    #print(end,st,par)
    while(end!=st):
        end=par[end]
        ans.append(end)
    ans.append(end1)
    print(len(ans))
    print(*ans)
        
                    
                    
                    
            

