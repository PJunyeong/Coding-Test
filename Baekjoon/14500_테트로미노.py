import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n)]

for i in range(n):
    nodes[i] += list(map(int, sys.stdin.readline().rstrip().split()))
blk_size = 0
for i in range(n):
    for j in range(m):
        # case1: --- 세 개 가로 구하고 각 구간에 한 개씩 블록을 한 개씩 붙인다.
        if j + 2 < m:
            block = nodes[i][j] + nodes[i][j+1] + nodes[i][j+2]
            if j + 3 < m: blk_size = max(blk_size, block+nodes[i][j+3])
            if i - 1 >= 0:
                blk_size = max(blk_size, block+nodes[i-1][j])
                blk_size = max(blk_size, block + nodes[i-1][j+1])
                blk_size = max(blk_size, block + nodes[i-1][j+2])
            if i + 1 < n:
                blk_size = max(blk_size, block+nodes[i+1][j])
                blk_size = max(blk_size, block+nodes[i+1][j+1])
                blk_size = max(blk_size, block+nodes[i+1][j+2])
        # case2: | 세로로 세 개 구하고 각 구간에 하나씩 블록 붙인다.
        if i + 2 < n:
            block = nodes[i][j] + nodes[i+1][j] + nodes[i+2][j]
            if i + 3 < n:
                blk_size = max(blk_size, block+nodes[i+3][j])
            if j - 1 >= 0:
                blk_size = max(blk_size, block+nodes[i][j-1])
                blk_size = max(blk_size, block + nodes[i+1][j - 1])
                blk_size = max(blk_size, block + nodes[i+2][j - 1])
            if j + 1 < m:
                blk_size = max(blk_size, block + nodes[i][j+1])
                blk_size = max(blk_size, block + nodes[i+1][j + 1])
                blk_size = max(blk_size, block + nodes[i+2][j + 1])
        #case3: -- 두 개 구하고 두 개 붙인다.
        if j + 1 < m:
            block = nodes[i][j] + nodes[i][j+1]
            if i+1 < n:
                blk_size = max(blk_size, block+nodes[i+1][j]+nodes[i+1][j+1])
                if j-1 >=0:
                    blk_size = max(blk_size, block+nodes[i+1][j-1] + nodes[i+1][j])
                if j+2 < m:
                    blk_size = max(blk_size, block+nodes[i+1][j+1]+nodes[i+1][j+2])
                if i-1>=0:
                    blk_size = max(blk_size, block+nodes[i-1][j]+nodes[i+1][j+1])
                    blk_size = max(blk_size, block+nodes[i-1][j+1]+nodes[i+1][j])
print(blk_size)