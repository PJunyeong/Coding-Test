from collections import deque

n, k = map(int, input().split())
queue = deque()

for i in range(1, n+1):
    queue.append(i)
    # 주어진 번호를 삽입

print('<', end='')
while len(queue) != 1:
    for _ in range(k-1):
        head = queue.popleft()
        queue.append(head)
        # 현재 큐 내의 k번째 사람을 타케팅하기 위해 그 앞의 사람들을 뒤로 보낸다.
    print(f"{queue.popleft()},", end=' ')
    # k번째 사람이므로 선택

print(f"{queue.popleft()}>")
# 출력 형태를 맞추기 위해 queue에 1명 남을 때까지 while 루프.