import sys 
input=sys.stdin.readline
import math 

 
n, q = map(int,input().split())
p = [0] + list(map(int,input().split()))
 
maxl = int(math.log2(10**9))
DP = [p]
for _ in range(maxl): 
    DP.append([DP[-1][i] for i in DP[-1]])
 
for _ in range(q):
    ans, k = map(int,input().split())
    while k:
        t = k & -k
        ans = DP[int(math.log2(t))][ans]
        k -= t
    print(ans)
