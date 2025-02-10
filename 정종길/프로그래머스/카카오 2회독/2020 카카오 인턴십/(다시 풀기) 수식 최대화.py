from itertools import permutations
from collections import defaultdict

def solution(expression):
    answer = 0
    oper = []
    
    if "-" in expression:
        oper.append("-")
    if "*" in expression:
        oper.append("*")
    if "+" in expression:
        oper.append("+")
    
    li_expression = expression.replace("-", " - ").replace("+", " + ").replace("*", " * ").split()
    
    for per in permutations(oper):
        ranks = { o : idx for idx, o in enumerate(per) }
        tmp_oper = []
        tmp_num = []
        for e in li_expression:
            if e.isdigit():
                tmp_num.append(int(e))
            else:
                while tmp_oper and ranks[tmp_oper[-1]] >= ranks[e]:
                    operation = tmp_oper.pop()
                    right = tmp_num.pop()
                    left = tmp_num.pop()
                    if operation == "*":
                        tmp_num.append(left * right)
                    elif operation == "-":
                        tmp_num.append(left - right)
                    else:
                        tmp_num.append(left + right)
                tmp_oper.append(e)
                    
        while tmp_oper:
            operation = tmp_oper.pop()
            right = tmp_num.pop()
            left = tmp_num.pop()
            if operation == "*":
                tmp_num.append(left * right)
            elif operation == "-":
                tmp_num.append(left - right)
            else:
                tmp_num.append(left + right)

        answer = max(abs(tmp_num[-1]), answer)
                
    return answer