import sys
input=sys.stdin.readline

N=int(input())
A=sorted(list(map(int, input().split())))
M=int(input())
B=list(map(int, input().split()))

for i in B:
    s=0
    e=len(A)-1
    result=False
    while s<=e:
        m=(s+e)//2
        if i==A[m]:
            result=True
            break
        elif i>A[m]:
            s=m+1
        else:
            e=m-1
    if result:
        print(1)
    else:
        print(0)