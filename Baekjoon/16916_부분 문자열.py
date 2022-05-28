import sys

s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()

def KMP(source, target):
    source_len = len(source)
    target_len = len(target)

    LPS = [0 for _ in range(target_len)]

    LPS_compute(target, LPS)

    source_idx, target_idx = 0, 0

    while source_idx < source_len:
        if target[target_idx] == source[source_idx]:
            source_idx += 1
            target_idx += 1
        else:
            if target_idx == 0:
                source_idx += 1
            else:
                target_idx = LPS[target_idx-1]

        if target_idx == target_len:
            return True
    return False
def LPS_compute(target, LPS):
    length = 0
    idx = 1
    while idx < len(target):
        if target[idx] == target[length]:
            length += 1
            LPS[idx] = length
            idx += 1
        else:
            if length == 0:
                LPS[idx] = 0
                idx += 1
            else:
                length = LPS[length-1]

if KMP(s, p): print(1)
else: print(0)