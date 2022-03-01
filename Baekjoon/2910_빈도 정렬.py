import sys

n, c = map(int, sys.stdin.readline().rstrip().split())
numbers = {}

for idx, num in enumerate(list(map(int, sys.stdin.readline().rstrip().split()))):
    num_info = numbers.get(num, [0, idx, num])
    num_cnt, num_idx, num = num_info
    num_cnt += 1
    numbers[num] = [num_cnt, num_idx, num]
    # 딕셔너리에 빈도와 처음 나온 인덱스, 숫자 기록

for num_cnt, num_idx, num in sorted(numbers.values(), key= lambda x: (-x[0], x[1])):
    # 빈도가 크고, 인덱스가 작은 순서대로 정렬
    result = f"{num} "*num_cnt
    print(result, end='')

