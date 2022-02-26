k, n = map(int, input().split())

lines = []

for _ in range(k):
    lines.append(int(input()))

lines.sort()
# 랜선 크기대로 정렬

start, end = 1, lines[-1]
# 각 랜선을 자를 수 있는 범위는 1 ~ 가장 큰 값
local_ns = []
while start <= end:
    mid = (start + end) // 2

    local_n = 0

    for line in lines:
        local_n += line // mid
        # mid는 해당 랜선을 자르는 단위.
        # local_n은 mid로 랜선을 각각 잘랐을 때 얻을 수 있는 개수 합

    if local_n >= n:
        # n개보다 많이 만들 수 있다면 mid를 기록해놓자.
        local_ns.append(mid)
        start = mid + 1
    else:
        end = mid - 1

print(max(local_ns))
# n개 이상 개수를 얻을 수 있는 길이 중 가장 큰 길이를 리턴한다.