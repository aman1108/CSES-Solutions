n,m=map(int,input().split())
vis=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    s=list(input())
    for j in range(m):
        if (s[j]=='#'):
            vis[i][j]=1

ans=0
for i in range(n):
    for j in range(m):
        if (vis[i][j]==0):
            ans+=1
            Q=[[i,j]]
            while(len(Q)!=0):
                x,y=Q.pop()
                if (x>0 and vis[x-1][y]==0):
                    vis[x-1][y]=1
                    Q.append([x-1,y])
                if (x<(n-1) and vis[x+1][y]==0):
                    vis[x+1][y]=1
                    Q.append([x+1,y])
                if (y>0 and vis[x][y-1]==0):
                    vis[x][y-1]=1
                    Q.append([x,y-1])
                if (y<(m-1) and vis[x][y+1]==0):
                    vis[x][y+1]=1
                    Q.append([x,y+1])
print(ans)

