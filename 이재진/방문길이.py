def solution(dirs):
    answer = 0
    dic = {"U": (-1,0), "D": (1,0), "R": (0,1), "L":(0,-1)}
    now = (0,0)
    v = set()
    for dir in dirs:
        d = dic[dir]
        next = (now[0]+d[0], now[1]+d[1])
        if -5 <= next[0] <= 5 and -5 <= next[1] <= 5:
            if (now, next) not in v and (next, now) not in v:
                answer += 1
                v.add((now, next))
                now = next
            else:
                now = next
    return answer
