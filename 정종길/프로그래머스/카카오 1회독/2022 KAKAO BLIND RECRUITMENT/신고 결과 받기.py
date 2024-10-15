def solution(id_list, report, k):
    N = len(id_list)
    reportLog = [set() for _ in range(N)]
    reportCnt = [0] * N
    Bens = []
    answer = [0] * N

    for row in report:
        A, B = row.split(" ")
        a = id_list.index(A)
        b = id_list.index(B)
        if B not in reportLog[a]:
            reportCnt[b] += 1
            reportLog[a].add(B)

    for i in range(N):
        if reportCnt[i] >= k:
            Bens.append(id_list[i])

    for i in range(N):
        for name in reportLog[i]:
            if name in Bens:
                answer[i] += 1

    return answer