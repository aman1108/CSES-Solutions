def bin_convert(x,n):
    val=bin(x).replace("0b","")
    if (len(val)<n):
        val='0'*(n-len(val))+val
    return val
n=int(input())
A=[0,1]
for i in range(n-1):
    x=len(A)-1
    val=pow(2,i+1)
    for j in range((2**(i+1))):
        A.append(val+A[x-j])
for val in A:
    print(bin_convert(val,n))
    
