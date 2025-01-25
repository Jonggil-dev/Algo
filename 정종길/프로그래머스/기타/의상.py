def solution(clothes):
    dic_clothes = {}
    answer = 1
    for cloth in clothes:
        dic_clothes[cloth[1]] = 0
    for cloth in clothes:
        dic_clothes[cloth[1]] += 1

    for cnt in dic_clothes.values():
        answer *= (cnt + 1)

    answer -= 1
    return answer