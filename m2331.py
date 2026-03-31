import sys
input=sys.stdin.readline

A,P=input().split()
P=int(P)
D=[A]

while True:
    x=0
    for i in range(len(A)):
        x+=int(A[i])**P
    if x in D:
        y=D.index(x)
        break
    else:
        D.append(x)
        A=str(x)

print(y)