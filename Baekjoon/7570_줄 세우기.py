import sys

n = int(sys.stdin.readline().rstrip())
kids = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
indices = [0 for _ in range(n+1)]
for idx in range(1, n+1):
    indices[kids[idx]] = idx
    # 현재 위치 인덱스 기록
    # (5, 2, 4, 1, 3) -> (4, 2, 5, 3, 1): 1이 4번에 위치하므로 인덱스 1에 4 기록
cnt = 0
answer = 0
for i in range(1, n):
    if indices[i] < indices[i+1]:
        # 현재 위치에 따라 "옮겨야 하는지" 여부 파악 가능. 연속 체크
        cnt += 1
        answer = max(cnt, answer)
    else:
        cnt = 0
        # 다시 0으로.

print(n-answer-1)
