import sys,math
input=sys.stdin.readline
def constree(val,A,segT):
    n,m=len(A),len(segT)
    for i in range(n):
        segT[val+i]=A[i]

    for i in range(val-1,0,-1):
        segT[i]=min(segT[(2*i)],segT[(2*i)+1])
    
def find(segT,l,r):
    ans=segT[r]
    while(l<r):
        #print(l,r)
        if (l%2!=0):
            ans=min(ans,segT[l])
            l+=1
            
        if (r%2==0):
            ans=min(ans,segT[r])
            r-=1
            
        l=l//2
        r=r//2
    if (l==r):
        ans=min(ans,segT[l])
    return ans
            
n,q=map(int,input().split())
A=list(map(int,input().split()))

val=pow(2,math.ceil(math.log2(n)))

segT=[10**9 for i in range(2*val)]
constree(val,A,segT)
#print(segT)
for i in range(q):
    l,r=map(int,input().split())
    print(find(segT,l+val-1,r+val-1))
