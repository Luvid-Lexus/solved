H,M=input().split()
H,M=int(H),int(M)

if H-1<0:
    H=23
else:
    H-=1

if M-45<0:
    M+=15
else:
    M-=45

print(f'{H} {M}')