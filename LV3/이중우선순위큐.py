import heapq
def solution(operations):
    heap = []
    max_cnt = 0
    min_cnt = 0
    heap_size = 0

    for operation in operations:
        if operation == "D 1":
            max_cnt += 1
        elif operation == "D -1":
            min_cnt += 1
        else:
            oper, digit = operation.split()
            digit = int(digit)
            heapq.heappush(heap, digit)
            heap_size += 1
            # 삽입되는 순서대로 최소 힙

        if max_cnt + min_cnt >= heap_size:
            max_cnt = 0
            min_cnt = 0
            heap_size = 0
            heap = []
            # 빈 힙에 삭제 명령어가 들어온 경우 모든 카운트와 힙을 리셋

    queue = []
    while heap:
        queue.append(heapq.heappop(heap))
        # heappop으로 순서대로 정렬된 수를 담은 큐

    if max_cnt + min_cnt >= len(queue): return [0, 0]
    # 남아 있는 수가 없을 때 디폴트 값 return
    queue = queue[min_cnt:len(queue)-max_cnt+1]
    # 남아 있는 수가 있을 때 정렬된 목록에서 앞에서/뒤에서 삭제할 개수만큼 없애고 최댓값, 최솟값을 return
    return [queue[-1], queue[0]]
