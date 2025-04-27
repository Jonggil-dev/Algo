from itertools import permutations

def solution(expression):
    answer = 0
    expression = expression.replace("*", " * ").replace("+", " + ").replace("-", " - ").split()

    for per in permutations(["+","*","-"], 3):
        priority = { oper : idx for idx, oper in enumerate(per) }
        o_stack, n_stack = [], []
        for data in expression:
            if data.isdigit():
                n_stack.append(int(data))
            else:
                while o_stack and priority[o_stack[-1]] >= priority[data]:
                    cal(o_stack, n_stack, priority)
                o_stack.append(data)
                
        while o_stack:
            cal(o_stack, n_stack, priority)

        answer = max(answer, abs(n_stack.pop()))
        
    return answer

def cal(o_stack, n_stack, priority):
    operator = o_stack.pop()
    right = n_stack.pop()
    left = n_stack.pop()
    if operator == "*":
        n_stack.append(left * right)
    elif operator == "+":
        n_stack.append(left + right)
    else:
        n_stack.append(left - right)
    return