import sys
input=sys.stdin.readline

N,J,S,H,K = map(int, input().split())
f3 = input().rstrip()
f2 = input().rstrip()
f1 = input().rstrip()
jump=0
d_jump=0
slide=0

for i in range(N):
    if f1[i] == '^':
        if f2[i] == '^':
            d_jump+=1
        else:
            jump+=1
    elif f2[i] == 'v':
        slide+=1

if jump>=J:
    jump-=J
    J=0
else:
    J-=jump
    jump=0

if slide>=S:
    slide-=S
    S=0
else:
    S-=slide
    slide=0    

if d_jump>=(J//2):
    d_jump-=J//2
else:
    d_jump=0

H-=K*(jump+slide+d_jump)

if H>0:
    print(H)
else:
    print(-1)