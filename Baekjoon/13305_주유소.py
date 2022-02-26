n = int(input())
stations = list(map(int, input().split()))
costs = list(map(int, input().split()))

total = 0
local_cost = costs[0]
# 첫 번째 주유소의 기름 가격

for i in range(n-1):
    if costs[i] < local_cost:
        local_cost = costs[i]
        # 현재 사용할 수 있는 주요소 (0~i) 중 가장 싼 가격을 고르자.
    total += local_cost * stations[i]
    # i번째 도시까지 주행할 때, 이 간격 내에 존재하는 가장 싼 기름을 사용하자.
    
print(total)