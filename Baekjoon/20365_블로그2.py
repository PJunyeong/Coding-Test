import sys

n = int(input())
paint = sys.stdin.readline().rstrip()
color = [0, 0]

if paint[0] == 'R': color[0] += 1
else: color[1] += 1
# 초깃값 color[0]에는 빨간색, color[1]에는 파란색 연속되지 않았을 때 카운트한다.
for i in range(1, n):
    if paint[i] != paint[i-1]:
        # 이전 색깔과 같다면 칠할 필요가 없다.
        if paint[i] == 'R': color[0] += 1
        else: color[1] += 1

print(min(color)+1)

