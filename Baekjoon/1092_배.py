import sys

n = int(sys.stdin.readline().rstrip())
weight_limits = list(map(int, sys.stdin.readline().rstrip().split()))
weight_limits.sort(reverse=True)
m = int(sys.stdin.readline().rstrip())
pq = []
weights = list(map(int, sys.stdin.readline().rstrip().split()))
weights.sort(reverse=True)

if weight_limits[0] < weights[0]: print(-1)
else:
    total = 0
    while weights:
        for limit in weight_limits:
            for weight in weights:
                if limit >= weight:
                    weights.remove(weight)
                    break
        total += 1
    print(total)