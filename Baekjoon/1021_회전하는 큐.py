from collections import deque

queue = deque()

n, m = map(int, input().split())

for i in range(1, n+1):
    queue.append(i)
    # queue: [1, 2, 3, 4, ..., n] 각 번호는 처음에 놓인 순서를 의미

m_pops = list(map(int, input().split()))
# 이 순서에 해당하는 번호가 0번 인덱스에 와야 추출 가능

cnt = 0

while m_pops:
    idx = queue.index(m_pops.pop(0))
    # 현재 주어진 큐에서 디큐해야 하는 값이 어디에 있는지 확인
    if idx == 0:
        queue.popleft()
        # 가장 앞이라면 cnt 더하지 않아도 추출 가능
    elif idx <= len(queue) // 2:
        for _ in range(idx):
            cnt += 1
            top = queue.popleft()
            queue.append(top)
        queue.popleft()
        # 앞 부분에 있다면 원하는 값이 0번 인덱스에 오도록 그 앞의 값을 뒤로 보낸다.
    else:
        length = len(queue) - idx
        for _ in range(length):
            cnt += 1
            bottom = queue.pop()
            queue.appendleft(bottom)
        queue.popleft()
        # 뒷 부분에 있다면 원하는 값이 0번 인덱스에 오도록 뒤의 값을 앞으로 보낸다.
print(cnt)


