def solution(stones, k):
    left, right = 0, max(stones)
    # 징검다리를 밟을 수 있는 최대값과 최솟값 사이에서 건널 수 있는 사람 수가 결정된다
    result = 0

    def jumpable(mid):
        # 연속된 k개의 다리를 건넌다.
        zero_cnt = 0
        for stone in stones:
            if stone < mid:
                zero_cnt += 1
                if zero_cnt == k: return False
                # 특정 다리가 '사람 수'보다 작으면 건너는 도중 0이 된다.
                # k개 이상 0이 연속으로 나오면 건널 수 없다는 뜻이다.
            else: zero_cnt = 0
        return True

    while left <= right:
        # 최솟값-최댓값 사이에서 건널 수 있는 사람 수를 빠르게 찾는 이분 탐색.
        mid = (left + right) // 2
        if jumpable(mid):
            result = max(result, mid)
            left = mid + 1
        else: right = mid - 1

    return result




stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
solution(stones, k)