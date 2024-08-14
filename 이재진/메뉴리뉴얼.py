from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        dic = {}
        for order in orders:
            if len(order) >= c:
                com = combinations(order,c)
                for i in com:
                    i = sorted(list(i))
                    i = "".join(i)
                    if i in dic:
                        dic[i] += 1
                    else:
                        dic[i] = 1
        if dic.keys():
            tmp = []
            max_num = 1
            for i in dic.keys():
                if max_num < dic[i]:
                    tmp = []
                    max_num = dic[i]
                    tmp.append(i)
                elif max_num > 1 and max_num == dic[i]:
                    tmp.append(i)
            for i in tmp:
                answer.append(i)
    answer.sort()
    return answer
