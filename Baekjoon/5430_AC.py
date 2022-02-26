from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    nums = input()[1:-1]

    if nums:
        queue = deque(list(map(int, nums.split(','))))
    else:
        queue = deque()
        # nums == []일 때에는 빈 디큐
    fliped = False
    error = False

    for cmd in p:
        if cmd == 'R':
            fliped = not fliped
            # 값이 있든 없든 flip 가능
        else:
            if not queue:
                error = True
                break
                # 값이 없을 때 꺼낸다면 error
            else:
                if fliped: queue.pop()
                else: queue.popleft()
                # 값이 있다면 fliped 여부에 맞춰서 pop한다.
    if error: print('error')
    else:
        if fliped: queue.reverse()

        print('[', end='')
        if queue: print(*queue, sep=',', end='')
        # 애스터리스크를 통해 queue 내용을 꺼내자. 구분자로 ','를 넣고 가로로 붙이기
        print(']')