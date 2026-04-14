import sys
input=sys.stdin.readline

N=int(input())
A=sorted(set(map(int,input().split())))
M=int(input())
B=set(map(int,input().split()))

for i in B:
    s=A[0]
    e=A[-1]
    while s<=e:
        m=(s+e)//2
        if i>=m:
            s=m+1
        else:
            e=m-1
    if e==i:
        print(1)
    else:
        print(0)