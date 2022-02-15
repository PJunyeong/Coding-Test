import math
def solution(n, k):
    line = [i for i in range(1, n+1)]
    result = []
    while line:
        fac = math.factorial(n-1)
        # 맨 앞의 자리수를 정하기 위해 건너뛸 크기: factorial n-1
        idx = int(k//fac)
        if k%fac == 0: idx -= 1
        # 나머지가 0일 때에는 다음 칸으로 넘어가지 않는다. 이때 리스트 line의 인덱스 -= 1을 해야 접근 가능
        k = k%fac
        # 지금 맨 앞에 설 사람이 빠진 뒤에 반복하기 위함
        result.append(line.pop(idx))
        n -= 1
    return result