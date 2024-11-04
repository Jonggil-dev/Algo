def solution(targets):
    answer = 0
    targets.sort(key = lambda x:x[0])
    print(targets)
    bound = 0
    for x,y in targets:
        if bound > x:
            bound = min(bound, y)
        else:
            bound = y
            answer += 1
    return answer
