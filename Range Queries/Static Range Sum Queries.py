n,q=map(int,input().split())
A=list(map(int,input().split()))
pref=[0 for i in range(n+1)]
for i in range(n):
    pref[i+1]=pref[i]+A[i]

for i in range(q):
    a,b=map(int,input().split())
    print(pref[b]-pref[a-1])
    
