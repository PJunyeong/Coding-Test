def solution(s):
    answer = []

    if len(s) == 1: return 1

    for i in range(1, len(s) // 2 + 1):
        # 압축 가능한 단위는 최대 전체 문자열 길이의 절반 (aa -> a/a 등)
        result = ''
        cnt = 1
        s_pre = s[:i]
        # s_pre는 앞에서 i번째 캐릭터까지
        for j in range(i, len(s), i):
            if s_pre == s[j:i + j]:
                cnt += 1
                # s_pre가 공통적으로 발견된다면 압축 가능
            else:
                if cnt != 1:
                    result += str(cnt) + s_pre
                    # 가능한 길이로 압축
                else:
                    result += s_pre
                    # 반복 없을 때에는 숫자 표시 X
                s_pre = s[j:i + j]
                cnt = 1
                # 길이 i 단위의 새로운 문자열 s_pre로 다음 문자열부터 검사한다.

        if cnt != 1:
            result += str(cnt) + s_pre
        else:
            result += s_pre
            # 위 for 문에서 s_pre 카운트가 남아 있을 때 결과값에 붙인다.
        answer.append(len(result))
        # 길이 i로 반복 압축했을 때 주어진 문자열을 len(result) 길이로 줄일 수 있다. 최소 길이를 return하자.
    return min(answer)