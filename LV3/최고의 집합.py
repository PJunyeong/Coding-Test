def solution(n ,s):
    q, r = divmod(s, n)
    if q==0: return [-1]
    result = [q]*n
    # s를 n개 자연수 합으로 표현할 때 가장 큰 곱이 나올 경우: 각 버킷에 담긴 자연수 간 차가 가장 작다
    # s=11 n=3 -> [n1, n2, n3] 중 [3, 3, 3]을 먼저 구해 놓고 나머지 2를 각 버킷에 1씩 나눠서 더해준다.
    idx = -1
    for _ in range(r):
        result[idx] += 1
        idx -= 1
    # 오름차순 정렬용
    return result