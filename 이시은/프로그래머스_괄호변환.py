# 프로그래머스 괄호 변환

# 최소 단위 균형잡힌 괄호 쌍 u, 나머지 v
# v를 계속 쪼개다가 v가 ""이 되면, 합치기
# 합칠 때는, u가 완전한 괄호면 u+v
# u가 균형잡힌 괄호면 (v)+u 앞 뒤 제거 후 괄호 뒤집기


def solution(p):
    def is_right(my_str):
        stack = []
        for s in my_str:
            if s == "(":
                stack.append(s)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return True

    def is_balance(my_str):
        if my_str.count("(") == my_str.count(")"):
            return True
        else:
            return False


    stack = []
    start = 0
    end = 1

    while start < end and end <= len(p):
        u = p[start:end]
        v = p[end:]
        if is_balance(u):
            stack.append(u)
            start = end
        end += 1
    stack.append(p[start:end])


    while len(stack) >= 2:
        v = stack.pop()
        u = stack.pop()
        if is_right(u):
            stack.append(u+v)
        else:
            tmp = "(" + v + ")"
            u = u[1:-1]
            while u:
                if u[0] == ")":
                    tmp += "("
                    u = u[1:]
                else:
                    tmp += ")"
                    u = u[1:]
            stack.append(tmp)

    answer = stack.pop()
    return answer


# p = "(()())()"
# p = ")("
p = "()))((()"

print(solution(p))


