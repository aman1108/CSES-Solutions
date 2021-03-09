n=int(input())
s=(n*(n+1))//2
if (s%2!=0):
    print("NO")

else:
    print("YES")
    A=[]
    B=[]
    x=n
    for i in range(n):
        if (i%4==0 or i%4==3):
            A.append(x)
        elif (i%4==1 or i%4==2):
            B.append(x)
        x=x-1
    print(len(A))
    print(*A)
    print(len(B))
    print(*B)
        
        
