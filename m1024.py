import sys
input=sys.stdin.readline

N,L=input().split()
N,L=int(N),int(L)

while L<=100:
    if N-L*(L-1)*0.5 > 0 and (N-L*(L-1)*0.5)%L == 0:
        x=int((N-L*(L-1)*0.5)%L)
        break
    else:
        L+=1

result=[]
for i in range(L):
    result.append(x+i)

print(*result)