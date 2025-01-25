def solution(begin, target, words):
    global visited, answer

    visited = set()
    answer = 1e9

    def dfs(changing, cnt):
        global visited, answer

        if changing == target:
            answer = min(answer, cnt)
            return answer

        for word in words:
            if word not in visited:
                if valid_change(changing, word):
                    visited.add(word)
                    dfs(word, cnt + 1)
                    visited.remove(word)

    dfs(begin, 0)

    if answer == 1e9:
        return 0

    return answer


def valid_change(now, after):
    check_cnt = 0
    for i in range(len(now)):
        if now[i] == after[i]:
            check_cnt += 1
    if check_cnt == (len(now) - 1):
        return True
    else:
        return False


