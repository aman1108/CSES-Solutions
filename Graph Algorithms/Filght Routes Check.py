from collections import defaultdict

n,m=map(int,input().split())
G=defaultdict(list)
G1=defaultdict(list)
for i in range(m):
    a,b=map(int,input().split())
    G[a].append(b)
    G1[b].append(a)

vis=[0]*(n+1)
val=[0]*(n+1)
val[1]=1
stk=[]
Q=[1]

while(len(Q)!=0):
    a=Q.pop()
    vis[a]=1
    stk.append(a)
    for i in G[a]:
        if (vis[i]==0):
            vis[i]=1
            Q.append(i)

        else:
            if (val[i]==1):
                val[a]=1

if (len(stk)!=n):
    print("NO")
    for i in range(1,n+1):
        if (vis[i]==0):
            print(1,i)
            break

else:
    vis=[0]*(n+1)
    val=[0]*(n+1)
    val[1]=1
    stk=[]
    Q=[1]
    G=G1
    while(len(Q)!=0):
        a=Q.pop()
        vis[a]=1
        stk.append(a)
        for i in G[a]:
            if (vis[i]==0):
                vis[i]=1
                Q.append(i)

            else:
                if (val[i]==1):
                    val[a]=1

    if (len(stk)!=n):
        print("NO")
        for i in range(1,n+1):
            if (vis[i]==0):
                print(i,1)
                break

    else:
        print("YES")
    
