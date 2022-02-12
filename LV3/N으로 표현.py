def calculator(j, k):
    tmp = []
    tmp.append(j+k)
    tmp.append(j*k)
    tmp.append(j-k)
    tmp.append(k-j)
    if k != 0: tmp.append(j//k)
    if j != 0: tmp.append(k//j)
    return tmp

def solution(N, number):
    dp = [[0]]
    # dp[n] -> n개의 N을 사용했을 때 만들어지는 수를 담은 배열
    for i in range(1, 9):
        tmp = set()
        base = int(str(N)*i)
        tmp.add(base)
        # 사칙연산 사용 X: N을 그대로 붙여 수를 생성

        for idx in range(1, i):
            for j in dp[idx]:
                for k in dp[i-idx]:
                    # N을 2개 쓴 경우 -> 1개 쓴 경우를 두 번 활용
                    # N을 3개 쓴 경우 -> 1개 쓴 경우 + 2개 쓴 경우 활용
                    # N을 4개 쓴 경우 -> 1개 쓴 경우 + 3개 쓴 경우 활용 / 2개 쓴 경우 + 2개 쓴 경우
                    #... N을 i개 쓴 경우 -> idx개 쓴 경우 + (i-idx)개 쓴 경우
                    for item in calculator(j, k):
                        tmp.add(item)
                        # 집합 tmp는 j와 k를 활용한 모든 사칙연산 결과를 포함 -> 중복값 제거
        if number in tmp:
            return i
        # N을 i개 쓴 tmp 차례에서 number 발견
        tmp = list(tmp)
        dp.append(tmp)

    return -1