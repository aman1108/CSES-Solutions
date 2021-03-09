T=int(input())
for _ in range(T):
    a,b=map(int,input().split())
    a,b=min(a,b),max(a,b)
    if (b>(2*a)):
        print("NO")
    else:
        spt=a//2
        if (a%2!=0):
            spt=spt+2
        if ((b-spt)%3!=0):
            print("NO")
        else:
            print("YES")
