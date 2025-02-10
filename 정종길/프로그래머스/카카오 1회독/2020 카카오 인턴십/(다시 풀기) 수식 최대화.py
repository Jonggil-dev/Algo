from itertools import permutations

def solution(expression):
    answer = 0
    expression = expression.replace("*", " * ").replace("-", " - ").replace("+", " + ").split()
    
    for opers in permutations(["*", "+", "-"]):
        oper_rank = {}
        for i, oper in enumerate(opers):
            oper_rank[oper] = 3 - i
        
        res = []
        stack = []
        
        for txt in expression:
            if txt.isdigit():
                res.append((txt))
            else:
                while stack and oper_rank[stack[-1]] >= oper_rank[txt]:
                    res.append(stack.pop())
                stack.append(txt)     
        
        while stack:
            res.append(stack.pop())
            
        for txt in res:
            if txt.isdigit():
                stack.append(int(txt))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if txt == "*":
                    stack.append(a * b)
                elif txt == "+":
                    stack.append(a + b)
                else:
                    stack.append(a - b)
                    
        answer = max(answer, abs(stack[0]))
        
    return answer