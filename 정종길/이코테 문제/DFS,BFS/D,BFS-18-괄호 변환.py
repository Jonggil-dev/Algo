'''
설계
1. 그냥 구현하기
2. 재귀로 return 되는 결과값 잘 생각하기
'''
def check_valid(u):
    cnt = 0
    for txt in u:
        if txt =="(":
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False

    if cnt > 0:
        return False
    else:
        return True

def check_balnce(u):
    cnt_1 = cnt_2 = 0
    for txt in u:
        if txt =="(":
            cnt_1 += 1
        else:
            cnt_2 += 1

    if cnt_1 and cnt_1 == cnt_2:
        return True

def reverse_txt(u):
    res = ""
    for txt in u:
        if txt =="(":
            res += ")"
        else:
            res += "("
    return res

def solution(p):
    answer =""
    if p == "":
        return answer
    u = ""
    for i in range(len(p)):
        u += p[i]
        if check_balnce(u):
            v = p[i+1:len(p)]

            if check_valid(u):
                return u + solution(v)
            else:
                return "(" + solution(v) + ")" + reverse_txt(u[1:-1])

print(solution(input()))