import sys
input=sys.stdin.readline
import math

N,K,M = map(int, input().split())
result=1

while N>0 or K>0:
    n_i,k_i = N%M, K%M
    N,K = N//M, K//M
    
    if n_i < k_i:
        result=0
        break
    else:
        result = (result * math.comb(n_i, k_i)) % M

print(result)