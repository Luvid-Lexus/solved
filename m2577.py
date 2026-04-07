import sys
input=sys.stdin.readline

A=int(input())
B=int(input())
C=int(input())

X=A*B*C
X=str(X)

for i in range(10):
    print(X.count(str(i)))