from itertools import combinations

n, m = map(int, input().split())

house = []
chicken = []

for i in range(n):
    for idx, j in enumerate(list(map(int, input().split()))):
        if j == 1: house.append([i, idx])
        elif j == 2: chicken.append([i, idx])
# 집, 치킨 집 좌표 입력

totals = []

combis = list(combinations(chicken, m))
# 치킨 집 중 m개를 선택하는 조합
for combi in combis:
    total = 0
    for h in house:
        h_row, h_col = h
        distance = 9999999
        for comb in combi:
            c_row, c_col = comb
            distance = min(distance, abs(h_row-c_row)+abs(h_col-c_col))
        # 주어진 치킨 집 중 각 집에서 가장 가까운 치킨 거리를 찾는다.
        total += distance
        # 모든 집의 치킨 거리의 합을 total이라 할 때
    totals.append(total)
    # 이 치킨 집 조합에서 생기는 치킨 거리의 합을 입력한다.
print(min(totals))
# 만들어진 치킨 거리 중 최솟값을 return
