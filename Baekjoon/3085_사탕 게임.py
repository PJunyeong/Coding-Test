import sys

n = int(sys.stdin.readline().rstrip())

candy = []
for _ in range(n):
    candy.append(list(sys.stdin.readline().rstrip()))

def get_cnt():
    global ans
    for base in range(n):
        cnt = 1
        for col in range(n-1):
            if candy[base][col] == candy[base][col+1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(cnt, ans)

        cnt = 1
        for row in range(n-1):
            if candy[row][base] == candy[row+1][base]:
                cnt += 1
            else:
                cnt = 1
            ans = max(cnt, ans)

ans = 0

for base in range(n):
    for col in range(n-1):
        candy[base][col], candy[base][col+1] = candy[base][col+1], candy[base][col]
        get_cnt()
        candy[base][col], candy[base][col + 1] = candy[base][col + 1], candy[base][col]
    for row in range(n-1):
        candy[row][base], candy[row+1][base] = candy[row+1][base], candy[row][base]
        get_cnt()
        candy[row][base], candy[row + 1][base] = candy[row + 1][base], candy[row][base]

print(ans)


