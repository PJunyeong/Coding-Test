def convert(n, k):
    result = ''
    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)
    return result[::-1]
    # n을 k진수로 변환하는 방법

def is_prime(num):
    if num == 1: return False

    for i in range(2, int(num**0.5)+1):
        # 효율성을 위해 제곱근까지만 확인한다.
        if num % i == 0: return False
    return True


def solution (n, k):
    k_ary= convert(n, k)
    # n을 k진수로 변환한다.
    total = 0
    for num in k_ary.split('0'):
        # k진수에서 0을 기준으로 split한 수가 소수인지 확인한다.
        if num != '' and num != '1':
            if is_prime(int(num)):
                total += 1
    return total