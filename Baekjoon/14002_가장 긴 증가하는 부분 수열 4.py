import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1 for i in range(n)]
answer = []
for i in range(n):
    # i번째 수 고정, 이 수보다 작은 앞의 j 수 합계 구하기
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

length = max(dp)
result = []

for idx in range(n-1, -1, -1):
    if length == dp[idx]:
        result.append(numbers[idx])
        length -= 1

result.reverse()
print(len(result))
print(*result)