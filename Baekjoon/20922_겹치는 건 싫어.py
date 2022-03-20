import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

left, right = 0, 0
ans = 0
counter = {}
while right < n:
    right_cnt = counter.get(numbers[right], 0)
    if right_cnt < k:
        right_cnt += 1
        counter[numbers[right]] = right_cnt
        right += 1
        # right 위치 수 카운트가 k개 이하이면 계속 확장 가능
    else:
        left_cnt = counter.get(numbers[left], 0)
        left_cnt -= 1
        counter[numbers[left]] = left_cnt
        left += 1
        # k보다 많아지면 k 이하가 될 때까지 left 커서를 오른쪽으로 움직이면서 현재 right 커서 수에 left 커서가 하나 올 떄까지 이동
    ans = max(ans, right - left)
    # ans는 가능한 수열 길이의 로컬 최댓값 유지

print(ans)