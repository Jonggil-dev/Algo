def solution(skill, skill_trees):
    answer = 0
    dic = dict()
    for i in range(len(skill)):
        dic[skill[i]] = i
    print(dic)
    for s in skill_trees:
        flag = 1
        tmp = 0
        for i in s:
            if i in skill:
                if dic[i] != tmp:
                    flag = 0
                    break
                else:
                    tmp += 1
        if flag:
            answer += 1
    return answer
