def solution(routes):
    routes.sort()
    answer = 0

    camera = routes[0]

    for i in routes[1:]:
        if i[0] <= camera[1]:
            camera = [i[0], min(i[1], camera[1])]
        else:
            camera = i
            answer += 1


    return answer+1