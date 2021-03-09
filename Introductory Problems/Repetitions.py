s=input()
ans=1
temp=1
for i in range(1,len(s)):
    if (s[i]==s[i-1]):
        temp=temp+1
    else:
        temp=1
    ans=max(ans,temp)
print(ans)
