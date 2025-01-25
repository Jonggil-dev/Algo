def solution(name, yearning, photo):
    answer = []

    for humans in photo:
        tmp = 0
        for human in humans:
            if human in name:
                tmp += yearning[name.index(human)]
        answer.append(tmp)

    return answer