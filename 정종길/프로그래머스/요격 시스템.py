def solution(targets):
    answer = 0    
    targets.sort(key = lambda x : (x[1], x[0]))
    s = e = 0
    
    for ns, ne in targets:
        if ns >= e:
            answer += 1
            e = ne
    
    return answer