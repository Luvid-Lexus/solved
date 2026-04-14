import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    H,W,N = map(int, input().split())
    a=(N-1)%H+1
    b=(N-1)//H+1
        
    print(f'{a}{b:02d}')