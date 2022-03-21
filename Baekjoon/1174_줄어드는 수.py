import sys

n = int(sys.stdin.readline().rstrip())
result = set()
# 중복 체크
number = []
def DFS():
    global result
    global number
    if number:
        result.add(int("".join(map(str, number))))
    for i in range(10):
        if not number or number[-1] > i:
            number.append(i)
            DFS()
            number.pop()
            # 백트래킹

DFS()

result = list(result)
result.sort()

if len(result) >= n: print(result[n-1])
else: print(-1)