import sys

m, n, l = map(int, sys.stdin.readline().rstrip().split())
guns = list(map(int, sys.stdin.readline().rstrip().split()))
guns.sort()
games = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    games.append([x, y])

games.sort()
cnt = 0
for game in games:
    x, y = game
    start = 0
    end = m-1
    while start < end:
        mid = (start + end) // 2
        if guns[mid] <= x:
            start = mid + 1
        else:
            end = mid
    # 사냥감의 x축 위치에 가장 가까운 총을 찾는다.
    if abs(guns[start]-x)+y <= l or abs(guns[start-1]-x)+y <= l: cnt += 1


print(cnt)

# hunted = [False for _ in range(n)]
# cnt = 0
#
# for gun in guns:
#     for idx, game in enumerate(games):
#         if hunted[idx]: continue
#         elif abs(game[0]-gun) + game[1] <= l:
#             cnt += 1
#             hunted[idx] = True
# print(cnt)
# hunted로 체크한 경우에는 60점 -> 이분 탐색으로 풀자




