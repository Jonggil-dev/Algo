# 프로그래머스 마법의 엘리베이터

def solution(storey):
    print(storey)
    if storey < 10:
        if storey <= 5:
            return storey
        else:
            return 10 - storey + 1

    if storey % 10 <= 5:
        cnt = storey % 10
        storey = round(storey/10)
        return cnt + solution(storey)
    else:
        cnt = 10 - storey % 10
        storey = round(storey/10)
        return cnt + solution(storey)


storey = 95
storey = 16
storey = 2554
storey = 1267

print(solution(storey))