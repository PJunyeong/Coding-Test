import sys

n = int(sys.stdin.readline().rstrip())
t = []
p = []
for _ in range(n):
    small_t, small_p = map(int, sys.stdin.readline().rstrip().split())
    t.append(small_t)
    p.append(small_p)

dp = [0 for _ in range(n+1)]
local_max = 0

for idx in range(n):
    local_max = max(local_max, dp[idx])
    # idx 날까지 얻을 수 있는 최대 비용
    last_work = t[idx] + idx
    # last_work까지 일해야 한다.
    if last_work > n: continue
    # 근무 불가능한 상담일 때
    dp[last_work] = max(local_max + p[idx], dp[last_work])
    # last_work 날 얻는 총 비용
    # local_max(idx날 일 아직 시작 X 얻는 로컬 최댓값) + p[idx] (last_work까지 일한다)
    # dp[last_work] idx 시작한 날 이외에도 last_work 끝나는 날 기록한 기존의 최댓값

print(max(dp))
