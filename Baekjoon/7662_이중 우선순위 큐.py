import heapq
import sys

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    k = int(sys.stdin.readline().rstrip())
    min_heap = []
    max_heap = []
    valid = [False for _ in range(1000001)]
    # cmd의 유니크한 인덱스로 이 명령어에 들어온 수가 유효한지 체크한다.
    for idx in range(k):
        cmd, num = sys.stdin.readline().rstrip().split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(min_heap, [num, idx])
            heapq.heappush(max_heap, [-1 * num, idx])
            valid[idx] = True
            # 이 idx에 들어온 num을 최대, 최소 힙 모두에 넣어준다.
            # 큐에 삽입했으므로 이 명령어는 현재 유효한 상태 True.
        else:
            # 유효한 값이 나올 때까지 팝하고, 삭제 가능하다면 삭제 후 이 인덱스는 더 이상 효과 X
            if num == 1:
                while max_heap and not valid[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    valid[heapq.heappop(max_heap)[1]] = False
            else:
                while min_heap and not valid[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                if min_heap:
                    valid[heapq.heappop(min_heap)[1]] = False

    # 모든 삽입/삭제 끝난 이후 각 힙에서 유효한 값만 남기고 삭제한다.
    while max_heap and not valid[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not valid[min_heap[0][1]]:
        heapq.heappop(min_heap)
    if not max_heap and not min_heap: print("EMPTY")
    else:
        # 각 최댓값, 최솟값을 힙에서 팝된 값을 통해 파악한다.
        max_num = heapq.heappop(max_heap)[0] * -1
        min_num = heapq.heappop(min_heap)[0]

        print(f"{max_num} {min_num}")



