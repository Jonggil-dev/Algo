def solution(k, tangerine):
    answer = 0
    tmp = {}

    for i in tangerine:
        tmp[i] = tmp.get(i, 0) + 1

    tmp = sorted(tmp.items(), key=lambda x: x[1], reverse=True)

    for i in tmp:
        k -= i[1]
        answer += 1
        if (k <= 0):
            break

    return answer