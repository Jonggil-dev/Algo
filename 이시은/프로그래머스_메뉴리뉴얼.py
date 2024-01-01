from itertools import combinations

def solution(orders, course):
    my_dict = {}
    counts = [2] * 9
    result = {}
    for order in orders:
        for n in course:
            result[n] = []
            combs = list(map(''.join, combinations(order, n)))
            for comb in combs:
                comb = ''.join(sorted(comb))
                my_dict[comb] = my_dict.get(comb, 0) + 1

    for key, value in my_dict.items():
        if value > counts[len(key)-2]:
            result[len(key)] = [key]
            counts[len(key)-2] = value
        elif value == counts[len(key)-2]:
            result[len(key)].append(key)

    # print(my_dict)
    # print(result)

    answer = []
    for res in result.values():
        answer.extend(res)

    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

orders = ["XYZ", "XWY", "WXA"]
course = [2]
print(solution(orders, course))

