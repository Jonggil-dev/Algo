import re

def solution(expressions):
    answer = []
    candidates = set(range(2,10))
    waitings = []
    
    for expression in expressions:
        if expression[-1] == "X":
            waitings.append(expression)
        each_candidates = check_expression(expression)
        candidates &= each_candidates
        
    for waiting in waitings:
        res = set()
        a, o, b  = re.findall(r'(\d+|[\+\-])',waiting)
        for candi in candidates:
            res.add(calculate(a, o, b, candi))
        
        if len(res) == 1:
            answer.append(waiting.replace("X", str(res.pop())))
        else:
            answer.append(waiting.replace("X", "?"))
            
    return answer

def check_expression(expression):
    each_candidates = set()
    if expression[-1] == "X":
        a, b = re.findall(r'(\d+)', expression)
        concat = map(int, set(a + b))
        mv = max(concat)
        for v in range(mv + 1, 10):
            each_candidates.add(v)
        return each_candidates
    
    a, o, b, c = re.findall(r'(\d+|[\+\-])',expression)
    concat = map(int, set(a + b + c))
    mv = max(concat)
    for v in range(mv + 1, 10):
        if calculate_check(a, o, b, c, v):
            each_candidates.add(v)
            
    return each_candidates

def calculate_check(a, o, b, c, v):
    num_a = num_b = num_c = 0
    for i in range(-1, - (len(a) + 1), -1):
        num_a += (v ** abs(i + 1)) * int(a[i])
    for j in range(-1, - (len(b) + 1), -1):
        num_b += (v ** abs(j + 1)) * int(b[j]) 
    for k in range(-1, - (len(c) + 1), -1):
        num_c += (v ** abs(k + 1)) * int(c[k])
    
    if o == "+":
        if num_a + num_b == num_c:
            return True
    else:
        if num_a - num_b == num_c:
            return True   
    return False

def calculate(a, o, b, verify_num):
    num_a = num_b = 0
    
    for i in range(-1, - (len(a) + 1), -1):
        num_a += (verify_num ** abs(i + 1)) * int(a[i])
    for j in range(-1, - (len(b) + 1), -1):
        num_b += (verify_num ** abs(j + 1)) * int(b[j]) 
    
    if o == "+":
        res = num_a + num_b
    else:
        res = num_a - num_b
        
    tmp =""
    while res:
        tmp = str((res %  verify_num)) + tmp
        res //= verify_num
    
    if not tmp:
        return 0
    
    return int(tmp)