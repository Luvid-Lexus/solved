N,X=input().split()
N,X=int(N),int(X)

L = [int(i) for i in list(input().split())]
l = []

for j in L:
    if j<X:
        l.append(j)

print(*l)