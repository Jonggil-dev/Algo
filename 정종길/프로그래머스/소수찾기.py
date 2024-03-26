from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, int(n ** (0.5)) + 1):
        if n % j == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    N = len(numbers)
    for i in range(1, N + 1):
        nums = set(permutations(numbers, i))
        for num in nums:
            if num[0] == '0':
                continue
            num = ''.join(num)
            if is_prime(int(num)):
                answer += 1

    return answer