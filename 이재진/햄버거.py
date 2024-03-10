def solution(ingredient):
    answer = 0
    ls = []
    for i in ingredient:
        ls.append(i)
        if len(ls) >= 4 and ls[-4:] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                ls.pop()
    return answer
