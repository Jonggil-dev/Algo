def solution(cards):
    answer = 0
    n = len(cards)
    visited = [0]*(n+1)
    ls = []
    for i in range(1, n+1):
        cur = i
        cnt = 0
        while not visited[cur]:
            visited[cur] = 1
            cnt += 1
            cur = cards[cur-1]
        ls.append(cnt)
    
    ls.sort()
    if len(ls) >= 2:
        answer = ls[-2] * ls[-1]
    return answer
