import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
people = [[] for _ in range(n+1)]
truth = list(map(int, sys.stdin.readline().rstrip().split()))
# 진실을 아는 사람들
people_known = [False for _ in range(n+1)]
party_visited = [False for _ in range(m)]
# 진실을 아는 사람들이 들른 파티
parties = []
for i in range(m):
    party = list(map(int, sys.stdin.readline().rstrip().split()))[1:]
    parties.append(party)
    for j in party:
        people[j].append(i)
        # 각 사람들이 방문한 파티 번호

if truth[0] == 0: print(m)
# 아무도 알지 못한다면 모든 파티에서 거짓말을 할 수 있다.
else:
    cnt = 0
    queue = deque(truth[1:])

    while queue:
        cur_person = queue.popleft()

        for party_num in people[cur_person]:
            # 진실을 아는 사람들이 방문한 파티 체크
            if not party_visited[party_num]:
                party_visited[party_num] = True
                cnt += 1
                # 이 파티를 들른 모든 사람들이 진실을 알 수 있기 때문
                for visiter in parties[party_num]:
                    if not people_known[visiter]:
                        people_known[visiter] = True
                        queue.append(visiter)

    print(m-cnt)
    # 모든 파티 개수 - 진실을 아는 사람들과 접촉한 이들이 들른 모든 파티의 수

