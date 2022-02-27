import math
import heapq

n, k = map(int, input().split())
# n은 [1, 1, 1, 1... 1]로 표시할 수 있다. 각 1+1 -> 2, 2+2 -> 4 등 2의 거듭제곱의 합으로 n을 표시한다.

purchased = 0
bottles = []

while n !=0:
    exp = 0
    while n - 2**exp >=0: exp += 1
    exp -= 1

    heapq.heappush(bottles, 2**exp)
    n -= 2**exp

while len(bottles) > k:
    bottle1 = heapq.heappop(bottles)
    bottle2 = heapq.heappop(bottles)
    # 가장 적은 수의 병을 구매해서 빈 병을 만들자.
    # 가장 적게 채워진 두 개의 물병을 bottles 힙에서 뽑는다.
    purchased += bottle2 - bottle1
    # bottle1에 bottle2보다 부족한 양을 채워서 합치면 빈 병 하나가 만들어진다.
    heapq.heappush(bottles, bottle2*2)
    # bottle1과 bottle2를 합쳐서 만들어진 병에 담긴 물의 양은 bottle2*2.

print(purchased)
