answer = -1


def solution(k, dungeons):
    def dfs(k, now, check, cnt):
        global answer

        if k >= dungeons[now][0]:
            k -= dungeons[now][1]
            cnt += 1

        if check == len(dungeons) - 1:
            answer = max(answer, cnt)

        for i in range(len(dungeons)):
            if not visited[i]:
                visited[i] = 1
                dfs(k, i, check + 1, cnt)
                visited[i] = 0

    visited = [0] * len(dungeons)

    for i in range(len(dungeons)):
        visited[i] = 1
        dfs(k, i, 0, 0)
        visited[i] = 0

    return answer
