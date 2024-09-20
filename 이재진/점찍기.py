import math
def cal(x,y):
    return math.sqrt(x**2 + y**2)

def solution(k, d):
    answer = 0
    for i in range(d+1):
        if i%k == 0:
            x = math.sqrt(d**2 - i**2)//k
            answer += x + 1
    
    return answer
