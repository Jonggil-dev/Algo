
def solution(N, computers):
    answer = 0
    chk=set()
    def func(now):
        ch=0
        for j in li[now]:
            if j not in chk:
                ch=1
                chk.add(j)
                func(j)
        return ch
    li=[[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if computers[i][j] and i!=j:
                li[i].append(j)

    for i in range(N):
        if i in chk:
            continue
        chk.add(i)
        func(i)
        answer+=1
    return answer