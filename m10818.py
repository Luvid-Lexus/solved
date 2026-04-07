N=int(input())
L=list(input().split())
L=[int(i) for i in L]
print(f'{min(L)} {max(L)}')