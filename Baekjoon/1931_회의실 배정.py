n = int(input())
times = []
for _ in range(n):
    start, end = map(int, input().split())
    times.append([start, end])
times.sort(key=lambda x:(x[1], x[0]))
# 회의가 빨리 끝나는 순서대로 정렬하자. 끝나는 시간이 같다면 빨리 시작하는 순서대로 고른다.
start, end = -1, -1
cnt = 0

for time in times:
    new_start, new_end = time
    # 지금 끝난 시점에서 시작 가능한 회의라면 고를 수 있다.
    if end <= new_start:
        end = new_end
        # 회의가 끝나는 기준은 이 새로 택한 회의가 마치는 시간이 된다.
        cnt += 1

print(cnt)