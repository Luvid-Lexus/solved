import sys
input=sys.stdin.readline

N=int(input())
l=[int(input()) for _ in range(N)]

l=sorted(l)
result=0

for i in range(len(l)):
    result+=abs(l[i]-i-1)

print(result)