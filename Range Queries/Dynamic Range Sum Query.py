import sys,math
input=sys.stdin.readline

def consTree(val,A,segT):
    n=len(A)
    for i in range(n):
        segT[val+i]=A[i]

    for i in range(val-1,0,-1):
        segT[i]=segT[(2*i)+1]+segT[2*i]
    

def findval(segT,l,r):
    ans=0
    while(l<r):
        if (l%2!=0):
            ans=ans+segT[l]
            l=l+1
        if (r%2==0):
            ans=ans+segT[r]
            r=r-1

        l=l//2
        r=r//2
    if (l==r):
        ans=ans+segT[l]
    return ans

def update(segT,ind,val,v):
    segT[ind+val]=v
    ind=ind+val
    ind=ind//2
    while(ind!=0):
        segT[ind]=segT[(2*ind)]+segT[(2*ind)+1]
        ind=ind//2
        
    
        
n,q=map(int,input().split())
A=list(map(int,input().split()))
val=pow(2,math.ceil(math.log2(n)))

segT=[0]*(2*val)
consTree(val,A,segT)


for i in range(q):
    a,b,c=map(int,input().split())
    if (a==1):
        update(segT,b-1,val,c)
    else:
        print(findval(segT,b+val-1,c+val-1))
