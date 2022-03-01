import sys

s = sys.stdin.readline().rstrip()

def is_palindrome(s):
    if len(s) % 2 == 0:
        right = len(s) // 2
        left = right - 1

    else:
        mid = len(s) // 2
        left = mid - 1
        right = mid + 1

    while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
        left -= 1
        right += 1

    if left == -1 and right == len(s): return True
    else: return False
    # 문자열 길이에 따라 팰린드롬 체크

if is_palindrome(s): print(len(s))
else:
    tmp = ''
    for i in range(len(s)):
        tmp += s[i]
        # tmp는 팰린드롬이 되기 위해 s 뒤에 거꾸로 더해줄 문자열
        if is_palindrome(s+tmp[::-1]): break

    print(len(s)+len(tmp))