def apnapow(x,y,mod):
    ans=1
    while(y!=0):
        if (y%2!=0):
            ans=(ans*x)%mod
            x=x*x
            y=(y-1)//2
        else:
            y=y//2
            x=x*x
        #print(x,y,ans)
    return ans

mod=(10**9)+7
n=int(input())
ans=apnapow(2,n,mod)
print(ans)
