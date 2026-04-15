import sys
input=sys.stdin.readline
import math

N,K,M = map(int, input().split())
pn=[]
pn_TF=[True]*(N+1)

for i in range(2,N+1):
    if pn_TF[i]:
        pn.append(i)
        for j in range(i**2,N+1,i):
            pn_TF[j]=False

def cnt_pn(N,n):
    cnt=0
    while N>0:
        cnt+=N//n
        N-=1
    return cnt

result=0

for n in pn:
    final_cnt = cnt_pn(N,n) - cnt_pn(K,n) - cnt_pn(N-K,n)
    if final_cnt < 0:
        result=math.comb(N,K)%M

print(result)