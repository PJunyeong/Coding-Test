import heapq
import sys

q_len = int(sys.stdin.readline().rstrip())
names = {}
total = 0
for _ in range(q_len):
    contents = list(sys.stdin.readline().rstrip().split())
    q = contents[0]
    name = contents[1]
    content = contents[2:]
    if q == '1':
        k = int(content[0])
        content = map(int, content[1:])
        name_content = names.get(name, [])
        for c in content:
            heapq.heappush(name_content, -1 * c)
        names[name] = name_content
        # 딕셔너리로 name 별 max_heap을 기록한다.
    else:
        b = int(*content)
        name_content = names.get(name, [])
        if len(name_content) <= b: b = len(name_content)
        for _ in range(b):
            total += -1 * heapq.heappop(name_content)
        # 딕셔너리로 얻은 name 별 max_heap에서 k개를 뽑아 더한다.

print(total)