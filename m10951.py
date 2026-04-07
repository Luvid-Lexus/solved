import sys

for line in sys.stdin:
    A, B = line.split()
    print(int(A) + int(B))