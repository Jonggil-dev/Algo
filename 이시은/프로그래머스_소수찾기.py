from itertools import permutations as perm


def solution(numbers):
    def is_prime(number):
        if number in [0, 1]:
            return False
        for i in range(2, int(number**(1/2) + 1)):
            if number % i == 0:
                return False
        return True

    answer = 0
    SET = set()
    for n in range(1, len(numbers) + 1):
        number_list = list(perm(numbers, n))
        for tmp in number_list:
            num = int(''.join(tmp))
            if is_prime(num) and num not in SET:
                answer += 1
                SET.add(num)

    return answer

numbers = '17'
print(solution(numbers))

'''
다른 사람 풀이
SET과 에라토스테네스의 체 조합

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1)))) # 가능 조합의 수를 모두 set 자료형에 담는다
    a -= set(range(0, 2)) # 0,1을 제외한다
    for i in range(2, int(max(a) ** 0.5) + 1): # 2 ~ sqrt(a의 최댓값) 중에서
        a -= set(range(i * 2, max(a) + 1, i)) # i의 배수를 set에서 제외한다 -> 소수가 아닌 수를 걸러내는 체
    return len(a)
'''