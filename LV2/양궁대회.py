def solution(n, info):
    result = [[info[0]+1], [0]]
    # 라이언 10점 획득 O / 획득 X
    for score, point in zip(info[1:], range(9, -1, -1)):
        new_result = []
        # 각 점수에 대한 라이언의 획득 여부를 모두 구한다(총 2^10개).
        while result:
            cur = result.pop(0)
            sel_a = cur + [0]
            # 남은 화살 수에 따라 0점을 쏜 수를 카운트.
            if point == 0 and n >= sum(cur):
                sel_a = cur + [n - sum(cur)]
            sel_b = cur + [score+1]
            new_result.append(sel_a)
            new_result.append(sel_b)
        result = new_result
    report = []
    for lions in result:
        if sum(lions) != n: continue
        # 라이언이 쏜 화살 수는 정확히 n개 만큼.
        l_score = 0
        a_score = 0
        for lion, apeach, point in zip(lions, info, range(10, -1, -1)):
            if lion or apeach:
                if lion > apeach: l_score += point
                else: a_score += point
        if l_score > a_score: report.append([l_score-a_score,lions])
        # 라이언이 어피치를 이길 때만 라이언의 '이길 수 있는 조합'을 체크.
    if not report: return [-1]
    # 라이언이 이길 수 없는 경우

    report.sort(reverse=True)
    result = []
    max_diff, max_report = report[0]

    for diff, rep in report:
        if diff == max_diff: result.append(rep[::-1])
        # 가장 큰 차이로 이기는 경우만 따로 분류한다.
        else: break
    result.sort(reverse=True)
    # 여러 조합이 있을 때 '낮은 점수'에 쏜 화살이 많을 경우를 골라야 한다.
    return result[0][::-1]