def solution(n, times):
    result = 0
    times.sort()
    # 심사 시간이 가장 "짧은" 심사관이 주어진 시간에 "가장 많은" 사람을 심사 가능 -> check 가산 부분에서 속도 향상

    left, right = 0, times[-1]*n
    # n명을 검사하는 데 걸리는 최소 시간 -> mid를 통해 "최소 시간" 찾기

    while left <= right:
        # 주어진 최소 mid를 찾아 result로 넘길 때까지 이분 탐색
        mid = (left + right) // 2
        # mid는 각 심사관에게 주어진 시간. 이 시간 내에 모든 사람 체크할 수 있는지 확인
        check = 0
        checkable = False

        for time in times:
            check += mid // time
            if check >= n:
                checkable = True
                # mid분으로 n명 검사 가능
                break

        if checkable:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result