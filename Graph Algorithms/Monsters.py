from collections import deque
n,m=map(int,input().split())
A=[]
vis=[[10**9 for i in range(m)] for j in range(n)]
vis1=[[-1 for i in range(m)] for j in range(n)]
Q=deque([])
st,en=0,0
for i in range(n):
    s=list(input())
    for j in range(m):
        if (s[j]=="M"):
            Q.append([i,j])
            vis[i][j]=0
        if (s[j]=="A"):
            st,en=i,j
            vis1[i][j]=0
    A.append(s)

while(len(Q)!=0):
    x,y=Q.popleft()
    if (x>0 and vis[x-1][y]==10**9 and A[x-1][y]!="#"):
        vis[x-1][y]=vis[x][y]+1
        Q.append([x-1,y])

    if (y>0 and vis[x][y-1]==10**9 and A[x][y-1]!="#"):
        vis[x][y-1]=vis[x][y]+1
        Q.append([x,y-1])

    
    if (y<(m-1) and vis[x][y+1]==10**9 and A[x][y+1]!="#"):
        vis[x][y+1]=vis[x][y]+1
        Q.append([x,y+1])

    if (x<(n-1) and vis[x+1][y]==10**9 and A[x+1][y]!="#"):
        vis[x+1][y]=vis[x][y]+1
        Q.append([x+1,y])


Q=[[st,en]]
st1,en1=0,0
flag=0
while(len(Q)!=0):
    x,y=Q.pop()
    if (x==0 or y==0 or x==n-1 or y==m-1):
        flag=1
        st1=x
        en1=y
        break
        
    if (x>0 and vis1[x-1][y]==-1 and A[x-1][y]!="#" and vis[x-1][y]>(vis1[x][y]+1)):
        vis1[x-1][y]=vis1[x][y]+1
        Q.append([x-1,y])

    if (y>0 and vis1[x][y-1]==-1 and A[x][y-1]!="#" and vis[x][y-1]>(vis1[x][y]+1)):
        vis1[x][y-1]=vis1[x][y]+1
        Q.append([x,y-1])

    if (y<(m-1) and vis1[x][y+1]==-1 and A[x][y+1]!="#" and vis[x][y+1]>(vis1[x][y]+1)):
        vis1[x][y+1]=vis1[x][y]+1
        Q.append([x,y+1])

    if (x<(n-1) and vis1[x+1][y]==-1 and A[x+1][y]!="#" and vis[x+1][y]>(vis1[x][y]+1)):
        vis1[x+1][y]=vis1[x][y]+1
        Q.append([x+1,y])

if (flag==0):
    print("NO")

else:
    print("YES")
    ans=[]
    Q=[[st1,en1]]
    while(len(Q)!=0):
        
        x,y=Q.pop()
        if (x==st and y==en):
            break
        mv=vis1[x][y]
        x1,y1=0,0
        val=""
        if (x>0 and vis1[x-1][y]!=-1 and vis1[x-1][y]<mv):
            x1,y1=x-1,y
            val="D"

        if (y>0 and vis1[x][y-1]!=-1 and vis1[x][y-1]<mv):
            x1,y1=x,y-1
            val="R"

        if (x<(n-1) and vis1[x+1][y]!=-1 and vis1[x+1][y]<mv):
            x1,y1=x+1,y
            val="U"
            
        if (y<(m-1) and vis1[x][y+1]!=-1 and vis1[x][y+1]<mv):
            x1,y1=x,y+1
            val="L"

        Q.append([x1,y1])
        ans.append(val)

    ans.reverse()
    print(len(ans))
    print(*ans,sep="")

 
        
