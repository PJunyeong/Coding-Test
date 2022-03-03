import sys

n = int(sys.stdin.readline().rstrip())
ropes = []

for _ in range(n):
    ropes.append(int(sys.stdin.readline().rstrip()))
ropes.sort(reverse=True)
local_max = ropes[0]
cnt = 2
for rope in ropes[1:]:
    if local_max < rope * cnt:
        # 로프의 로컬 최솟값 rope, cnt는 이 로프 길이 이상의 모든 로프 개수
        # 즉 rope * cnt는 이 로프를 사용할 때 들 수 있는 무게의 최댓값
        local_max = rope * cnt
    cnt += 1

print(local_max)

