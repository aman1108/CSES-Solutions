from collections import deque
n,m=map(int,input().split())
vis=[[10**9 for i in range(m)] for j in range(n)]
start,end=[0,0],[0,0]
for i in range(n):
    s=list(input())
    for j in range(m):
        if (s[j]=='#'):
            vis[i][j]=-1
        elif (s[j]=='A'):
            start=[i,j]
        elif (s[j]=='B'):
            end=[i,j]

Q=deque([end])
vis[end[0]][end[1]]=0
while(len(Q)!=0):
    x,y=Q.popleft()
    if (x>0 and vis[x-1][y]==(10**9)):
        vis[x-1][y]=min(vis[x-1][y],1+vis[x][y])
        Q.append([x-1,y])
    if (x<(n-1) and vis[x+1][y]==(10**9)):
        vis[x+1][y]=min(vis[x][y]+1,vis[x+1][y])
        Q.append([x+1,y])
    if (y>0 and vis[x][y-1]==(10**9)):
        vis[x][y-1]=min(vis[x][y]+1,vis[x][y-1])
        Q.append([x,y-1])
    if (y<(m-1) and vis[x][y+1]==(10**9)):
        vis[x][y+1]=min(vis[x][y]+1,vis[x][y+1])
        Q.append([x,y+1])
    
    
if (vis[start[0]][start[1]]==10**9):
    print("NO")

else:
    print("YES")
    print(vis[start[0]][start[1]])
    #print(vis)
    Q=[start]
    ans=[]
    while(len(Q)!=0):
        x,y=Q.pop()
        #print(x,y)
        vis[x][y]=10**9
        if ([x,y]==end):
            break
        mv=10**9
        sym=""
        x1,y1=0,0
        if (x>0 and vis[x-1][y]!=-1):
            if (vis[x-1][y]<mv):
                mv=vis[x-1][y]
                sym="U"
                x1,y1=x-1,y
            
        if (x<(n-1) and vis[x+1][y]!=-1):
            if (vis[x+1][y]<mv):
                mv=vis[x+1][y]
                sym="D"
                x1,y1=x+1,y
            
        if (y>0 and vis[x][y-1]!=-1):
            if (vis[x][y-1]<mv):
                mv=vis[x][y-1]
                sym="L"
                x1,y1=x,y-1
            
        if (y<(m-1) and vis[x][y+1]!=-1):
            if (vis[x][y+1]<mv):
                mv=vis[x][y+1]
                sym="R"
                x1,y1=x,y+1
        vis[x1][y1]=10**9
        
        Q=[[x1,y1]]
        ans.append(sym)
    print(*ans,sep="")
            

