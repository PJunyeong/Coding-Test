import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

infos = {}

for _ in range(n):
    site, pw = sys.stdin.readline().rstrip().split()
    infos[site] = pw

for _ in range(m):
    site = sys.stdin.readline().rstrip()
    print(infos[site])