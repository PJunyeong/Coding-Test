import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
bench = list(sys.stdin.readline().rstrip())
people = []
for idx, b in enumerate(bench):
    if b == 'P': people.append(idx)
cnt = 0
for i in people:
    for j in range(-k, k+1):
        if i + j < 0 or i + j >= len(bench): continue
        if bench[i+j] == 'H':
            bench[i+j] = 'P'
            cnt += 1
            break
print(cnt)