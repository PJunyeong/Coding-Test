import sys
from collections import deque

def get_prime():
    primes = [True for i in range(10000)]
    for i in range(2, int(10000**0.5)+1):
        if primes[i] == True:
            for j in range(i+i, 10000, i):
                primes[j] = False
    return [i for i in range(1000, 10000) if primes[i] is True]
# 에라토스테네스의 체로 네 자리 수 소수 리턴

def BFS(target, goal):
    goal = list(str(goal))
    queue = deque()
    visited = set()
    visited.add(target)
    target = list(str(target))
    queue.append([target, 0])
    while queue:
        cur_num, cur_cnt = queue.popleft()
        if cur_num == goal: return cur_cnt

        for i in range(4):
            if i == 0:
                for j in range(1, 10):
                    next_num_str = [str(j)] + cur_num[i+1:]
                    next_num = int(''.join(next_num_str))
                    if cur_num[i] != j and next_num not in visited and next_num in primes:
                        visited.add(next_num)
                        queue.append([next_num_str, cur_cnt + 1])
            #             첫 번째 자리 수는 0으로 대체할 수 없다.
            else:
                for j in range(0, 10):
                    next_num_str = cur_num[:i] + [str(j)] + cur_num[i+1:]
                    next_num = int(''.join(next_num_str))
                    if cur_num[i] != j and next_num not in visited and next_num in primes:
                        visited.add(next_num)
                        queue.append([next_num_str, cur_cnt + 1])
    #                     현재 자리를 다른 수로 변경 가능할 때(현재 수와 다르고, 방문하지 않았고, 바꾼 자리로 만든 네 자리 수가 소수일 때)
    return "Impossible"

primes = set(get_prime())
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    target, goal = map(int, sys.stdin.readline().rstrip().split())
    print(BFS(target, goal))