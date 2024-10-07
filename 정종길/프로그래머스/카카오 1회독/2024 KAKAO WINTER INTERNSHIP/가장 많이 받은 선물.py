def solution(friends, gifts):
    answer = 0
    N = len(friends)
    giftsTable = [[0] * N for _ in range(N)]
    indicesTable = [[0] * 3 for _ in range(N)]
    results = [0] * N

    for info in gifts:
        i, j = info.split()
        a = friends.index(i)
        b = friends.index(j)
        giftsTable[a][b] += 1
        indicesTable[a][0] += 1
        indicesTable[b][1] += 1

    for row in indicesTable:
        row[2] = row[0] - row[1]

    for i in range(N):
        for j in range(i + 1, N):
            if (giftsTable[i][j] == 0 and giftsTable[j][i] == 0) or (giftsTable[i][j] == giftsTable[j][i]):
                if indicesTable[i][2] == indicesTable[j][2]:
                    continue
                if indicesTable[i][2] > indicesTable[j][2]:
                    results[i] += 1
                else:
                    results[j] += 1

            if giftsTable[i][j] > giftsTable[j][i]:
                results[i] += 1
            elif giftsTable[i][j] < giftsTable[j][i]:
                results[j] += 1

    answer = max(results)
    return answer