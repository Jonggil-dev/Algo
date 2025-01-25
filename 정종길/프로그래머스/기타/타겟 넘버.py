def solution(numbers, target):
    def dfs(L, tot):
        nonlocal answer, N, target, numbers
        if L == N - 1:
            if tot == target:
                answer += 1
            return
        dfs(L + 1, tot + numbers[L])
        dfs(L + 1, tot - numbers[L])

    answer = 0
    N = len(numbers)
    dfs(-1, 0)

    return answer