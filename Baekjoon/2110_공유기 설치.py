n, c = map(int, input().split())

x = []

for _ in range(n):
    x.append(int(input()))

x.sort()
# 집 위치대로 정렬

start, end = 1, x[-1]-x[0]
# 가장 작은 간격 1부터 가장 긴 간격 (가장 멀리 있는 집 사이 간 거리) 범위
lengths = []

while start <= end:

    mid = (start + end) // 2
    # mid는 공유기 사이의 거리
    cnt = 1
    # 사용할 공유기의 개수 cnt
    cur = x[0]

    for house in x[1:]:
        distance = house - cur
        # 비교하려는 집과 현재 기준 집 사이의 거리
        if distance >= mid:
            # 집들 간의 거리가 공유기 간격보다 크다면 카운트
            cur = house
            # 새로운 공유기를 사용해야 하므로 집 기준점을 다시 변경.
            cnt += 1

    if cnt >= c:
        # 사용한 공유기 개수가 c보다 클 때 이 mid를 간격으로 사용할 수 있다.
        lengths.append(mid)
        start = mid + 1
    else:
        end = mid - 1

print(max(lengths))
# 공유기 간격 중 가장 큰 값을 리턴한다.


