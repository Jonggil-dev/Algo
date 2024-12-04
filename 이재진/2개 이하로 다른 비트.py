from collections import deque
def cal(x):
    string = str(bin(x))[2:]
    q = deque(string)
    for i in range(len(q)-1,-1,-1):
        if q[i] == "0":
            q[i] = "1"
            if i != len(q)-1:
                q[i+1] = "0"
            tmp = "".join(q)
            ans = int("0b"+tmp,2)
            return ans
    q[0] = "0"
    q.appendleft("1")
    tmp = "".join(q)
    ans = int("0b"+tmp,2)
    print(bin(5))
    return ans
        
        
    
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(cal(i))
    return answer
