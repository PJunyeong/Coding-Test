import sys
from collections import deque
from collections import Counter

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    # m이 커서
    preferences = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    preference_counter = Counter(preferences)
    preference_list = list(preference_counter.keys())
    preference_list.sort(reverse=True)
    # 현재 프린트 내 문서 중요도를 맨 앞에 있는 문서 중요도와 비교해서 개수 및 최고 중요도 파악. 내림차순 정렬
    print_cnt = 0
    # 현재 출력된 문서 수
    local_max = preference_list.pop(0)
    local_max_cnt = preference_counter.get(local_max)

    while preferences:
        preference = preferences.popleft()
        if preference == local_max:
            print_cnt += 1
            local_max_cnt -= 1
            if local_max_cnt == 0:
                # 큐에 있는 문서 중 최고 우선순위 문서가 모두 출력되었음
                if preference_list: local_max = preference_list.pop(0)
                local_max_cnt = preference_counter.get(local_max)
            if m == 0: break
            # 출력된 문서가 케이스라면 break
            else: m -= 1
            # 앞의 문서가 출력되었으므로 앞으로 한 칸 당긴다.
        elif preference < local_max:
            preferences.append(preference)
            if m == 0: m = len(preferences)-1
            # 케이스 문서를 맨 뒤로 넣었다
            else: m -= 1

    print(print_cnt)


