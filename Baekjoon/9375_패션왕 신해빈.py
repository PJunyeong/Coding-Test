import sys
from itertools import combinations

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    dresses = {}
    for _ in range(n):
        dress_name, dress_type = sys.stdin.readline().rstrip().split()
        dress_num = dresses.get(dress_type, 0)
        dress_num += 1
        dresses[dress_type] = dress_num
    dress_nums = list(dresses.values())
    # 각 타입이 인덱스로, 옷의 개수가 값인 리스트 dress_nums
    total = 1
    for num in dress_nums:
        total *= (num+1)
        # 옷을 안 입는 경우까지 포함해서 1을 더해주고, 모든 경우를 구하기 위해 곱
    print(total-1)
    # total은 각 타입별 옷을 하나씩 써서 만들 수 있는 모든 조합. 이중 옷을 아예 안 입는 경우 1을 빼준다.
