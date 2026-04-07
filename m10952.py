import sys
input=sys.stdin.readline

while True:
    A,B=input().split()
    if A==B=='0':
        break
    else:
        print(int(A)+int(B))