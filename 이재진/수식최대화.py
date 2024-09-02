from itertools import permutations
import copy
from collections import deque
def solution(expression):
    answer = 0
    exp = []
    tmp = ""
    for i in expression:
        if i in "*-+":
            exp.append(int(tmp))
            exp.append(i)          
            tmp = ""
        else:
            tmp += i
    exp.append(int(tmp))
    
    for per in permutations(["*", "+", "-"]):
        ls = copy.deepcopy(exp)
        for i in per:
            tmp = []
            for j in ls:
                if tmp and tmp[-1] == i:
                    tmp.pop()
                    if i == "*":
                        tmp.append(tmp.pop()*j)
                    elif i == "+":
                        tmp.append(tmp.pop()+j)
                    elif i == "-":
                        tmp.append(tmp.pop()-j)
                else:
                    tmp.append(j)
            ls = tmp
        if answer < abs(ls[0]):
            answer = abs(ls[0])
            
        

    return answer
