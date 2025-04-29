def solution(p):
    answer = check_parentheses(p)
    return answer

def check_parentheses(p):
    flag, cnt, st  = True, 0, 0
    ans = ""
    i = 0
    while i < len(p):
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                flag = False
                
        if cnt == 0:
            if flag:
                ans += p[st: i+1]
                flag = True
                st = i + 1
            else:
                u, v = p[st + 1 : i], p[i + 1:]
                ans += "(" + check_parentheses(v) + ")" + reverse(u)
                return ans
        i += 1
        
    return ans

                
def reverse(u):
    tmp = ""
    for data in u:
        if data == "(":
            tmp += ")"
        else:
            tmp += "("
    return tmp