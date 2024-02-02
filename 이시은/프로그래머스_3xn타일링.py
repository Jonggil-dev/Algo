def solution(n):
    if n == 2:
        return 3

    if n % 2 == 1:
        return 0
    else:
        memo = [1, 3]
        idx = 1
        while True:
            memo.append(memo[idx] * 4 - memo[idx-1])
            idx += 1
            if len(memo) == n//2 + 1:
                return memo[-1] % 1000000007

print(solution(2))
print(solution(3))
print(solution(4))
print(solution(6))
print(solution(8))