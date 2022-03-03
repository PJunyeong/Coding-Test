import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    people = []
    for idx in range(n):
        rank1, rank2 = map(int, sys.stdin.readline().rstrip().split())
        people.append([rank1, rank2])

    people.sort()
    # 서류 순위대로 정렬
    target = people[0][1]
    # 서류 심사 1위는 합격 보장
    # 로컬 최솟값(순위이므로)을 구해가면서 합격 가능한지 체크한다.
    cnt = 1

    for person in people[1:]:
        rank1, rank2 = person
        if rank2 < target:
            # 이 사람이 현재까지 중에서 가장 높은 순위
            cnt += 1
            # 서류 순위를 밀린 사람들보다 면접 순위가 높기 때문
            target = rank2

    print(cnt)

