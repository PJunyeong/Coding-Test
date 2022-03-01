import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
A = set(map(int, sys.stdin.readline().rstrip().split()))
B = set(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0

inter_ab = A.intersection(B)
len_inter_ab = len(inter_ab)

print(a + b - 2* len_inter_ab)


