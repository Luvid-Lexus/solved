import sys
input=sys.stdin.readline
import math

N,K = map(int, input().split())
result=0

for i in range(1,N):
    result+=math.comb(i,K-1)

print(result)