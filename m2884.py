H,M=input().split()
H,M=int(H),int(M)

if M-45<0:
    M+=15
    H-=1
else:
    M-=45

print(f'{H} {M}')