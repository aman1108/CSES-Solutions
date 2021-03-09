n,m,k=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()
j=0
ans=0
for i in range(n):
    while(j<m and (A[i]> (B[j]+k))):
        j=j+1

    if (j<m and A[i]<=(B[j]+k) and A[i]>=(B[j]-k)):
        j=j+1
        ans=ans+1
print(ans)
    
