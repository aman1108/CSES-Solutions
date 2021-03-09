s=list(input())
G={}
for i in s:
    try:
        G[i]=G[i]+1
    except:
        G[i]=1
flag=0
if (len(s)%2!=0):
    flag=1
A=[]
for i in G:
    A.append([G[i]%2,i])
    if (G[i]%2!=0):
        flag-=1
A.sort()
if (flag<0):
    print("NO SOLUTION")
else:
    pref=[]
    suf=[]
    for val in A:
        if (val[0]==0):
            for i in range(0,G[val[1]],2):
                pref.append(val[1])
                suf.append(val[1])
        else:
            for i in range(0,G[val[1]]-1,2):
                pref.append(val[1])
                suf.append(val[1])
            pref.append(val[1])
    
    suf=suf[::-1]
    print(*(pref+suf),sep="")
        
