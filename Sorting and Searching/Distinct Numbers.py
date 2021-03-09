n=int(input())
A=list(map(int,input().split()))
G={}
ans=0
for i in A:
    if i not in G:
        G[i]=1
        ans+=1
print(ans)
