def solution(words):
    N = len(words)
    words.sort()
    result = [0] * N

    for i in range(N - 1):
        a = len(words[i])
        b = len(words[i + 1])
        for j in range(min(a, b)):
            if words[i][j] != words[i + 1][j]:
                j -= 1
                break

        result[i] = max(result[i], min(a, j + 2))
        result[i + 1] = max(result[i + 1], j + 2)

    return sum(result)