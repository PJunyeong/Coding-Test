import sys

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()
B.sort(reverse=True)

total = 0
for a, b in zip(A, B):
    total += a * b

print(total)
