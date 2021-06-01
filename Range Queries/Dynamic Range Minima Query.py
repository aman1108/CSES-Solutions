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
            
        if (r%2!=0):
            r-=1
            ans=min(ans,segT[r])
            
        l=l//2
        r=r//2
    
    return ans

def update(segT,ind,val,c):
    segT[ind+val]=c
    ind=(ind+val)//2
    while(ind!=0):
        segT[ind]=min(segT[(2*ind)],segT[(2*ind)+1])
        ind=ind//2
    
n,q=map(int,input().split())
A=list(map(int,input().split()))

val=pow(2,math.ceil(math.log2(n)))

segT=[10**9 for i in range(2*val)]
constree(val,A,segT)
#print(segT)
for i in range(q):
    a,b,c=map(int,input().split())
    if (a==1):
        update(segT,b-1,val,c)
    else:
        print(find(segT,b+val-1,c+val-1))
