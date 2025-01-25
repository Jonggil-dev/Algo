def solution(name):
    answer = 0
    n = len(name)

    for ch in name:
        answer += min(ord(ch) - ord('A'), abs(ord('Z') - ord(ch)) + 1)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        dist = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + dist)

    return answer + move