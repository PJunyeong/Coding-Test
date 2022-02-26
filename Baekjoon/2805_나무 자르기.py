n, m = map(int, input().split())

trees = list(map(int, input().split()))
trees.sort(reverse=True)
# 해당 높이보다 작다면 자를 수 없으므로 내림차순으로 정렬하자.

start, end = 0, trees[0]
# 자를 수 있는 높이는 0부터 가장 큰 나무의 높이까지

heights = []
while start <= end:
    mid = (start+end) // 2
    total = 0

    for tree in trees:
        if tree >= mid: total += tree - mid
        # mid 높이로 나무를 자를 때 얻을 수 있는 목재 길이의 합
        else: break
        # 더 이상 자를 수 없다면 그만둔다.

    if total >= m:
        # mid 높이로 잘랐을 때 total 길이의 목재를 얻을 수 있다. m보다 크다면 heights에 mid를 기록
        heights.append(mid)
        # 자르는 높이를 좀 더 높여보자.
        start = mid + 1
    else:
        end = mid - 1

print(max(heights))
# m 길이 이상의 목재를 얻을 수 있는 높이 중 가장 큰 값을 리턴한다.