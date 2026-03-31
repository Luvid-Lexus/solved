import sys
input=sys.stdin.readline

A,P=input().split()
P=int(P)
D=[]

while True:
    x=0
    for i in range(len(A)):
        x+=int(A[i])**P
    print(x)
    if x in D:
        y=D.index(x)
        break
    else:
        D.append(x)
        A=x

print(y)