import sys
input=sys.stdin.readline

N=int(input())
l=[]

for _ in range(N):
    l.append(int(input()))

l=sorted(l)
result=0

for i in range(len(l)):
    result+=abs(l[i]-i-1)

print(result)