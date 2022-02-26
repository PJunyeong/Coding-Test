import heapq

n = int(input())
A = []
for num in map(int, input().split()):
    heapq.heappush(A, num)
sorted_A= []

while A:
    sorted_A.append(heapq.heappop(A))
# 리스트 정렬

m = int(input())
for num in map(int, input().split()):
    # num이 sorted_A에 존재하는지 이분 탐색으로 찾는다.
    start, end = 0, n-1

    is_in = False
    while start <= end:
        mid = (start + end) // 2
        if num == sorted_A[mid]:
            is_in = True
            break
        elif num < sorted_A[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if is_in: print(1)
    else: print(0)
