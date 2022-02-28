from itertools import combinations

for _ in range(4):

    nations = [[] for _ in range(6)]
    games = list(map(int, input().split()))

    for i in range(6):
        for j in range(3):
            nations[i].append(games.pop(0))
    # i번 국가는 nations[i], 0, 1, 2는 각각 승리, 무승부, 패배 카운트 기록

    is_possible = []
    cases = list(combinations(range(6), 2))
    # 6개 국가별 경기 조합

    def backtracking(turn_num):
        if turn_num == len(cases):
            # 특정 경기에서 (승패, 무무, 패승) 중 한 가능성을 택한 뒤 이를 따라왔을 때 마지막 라운드
            possible = 1
            for i in range(6):
                for j in range(3):
                    if nations[i][j] != 0:
                        possible = 0
                        break
                        # 마지막 라운드까지 마쳤을 때 모든 카운트는 0이어야 정상적인 경기
            is_possible.append(possible)
            return

        n1, n2 = cases[turn_num]
        for x, y in ((0, 2), (1, 1), (2, 0)):
            if nations[n1][x] > 0 and nations[n2][y] > 0:
                # 승패, 무무, 패승이 가능할 때 이를 마킹(즉 각각 카운트를 1씩 빼준다)
                nations[n1][x] -= 1
                nations[n2][y] -= 1
                backtracking(turn_num + 1)
                # n1, n2 두 국가 간 경기에서 3가지 케이스가 모두 일어날 수 있기 때문에 복구해준다.
                nations[n1][x] += 1
                nations[n2][y] += 1


    backtracking(0)

    if 1 in is_possible: print(1)
    else: print(0)


