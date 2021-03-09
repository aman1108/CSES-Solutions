n=int(input())
A=list(map(int,input().split()))
s=sum(A)
print(((n*(n+1))//2)-s)
