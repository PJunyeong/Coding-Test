def solution(triangle):
    dp = [0] + [0] * (sum(range(1, len(triangle) + 1)))
    dp[1] = triangle[0][0]
    # level_1 (꼭대기)

    idx = 1
    left_offset = -2
    right_offset = -1
    # 현재 dp 인덱스 커서 및 상위 level로 이어진 인덱스 커서

    for i in range(1, len(triangle)):
        # level_2부터  level_n(바닥)
        idx += 1
        dp[idx] = triangle[i][0] + dp[idx + right_offset]
        # leftmost, rightmost는 각각 오른쪽, 왼쪽 대각선 위의 노드 선택
        for j in range(1, len(triangle[i]) - 1):
            idx += 1
            dp[idx] = triangle[i][j] + max(dp[idx + left_offset], dp[idx + right_offset])
            # 중간 노드는 연결된 왼쪽, 오른쪽 노드 중 최댓값을 선택
        idx += 1
        dp[idx] = triangle[i][-1] + dp[idx + left_offset]

        left_offset -= 1
        right_offset -= 1

    return max(dp)