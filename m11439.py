import sys
input=sys.stdin.readline
import math

N,K,M = map(int, input().split())
result=0

for i in range(K-1,N):
    result+=math.comb(i,K-1) % M

print(result%M)