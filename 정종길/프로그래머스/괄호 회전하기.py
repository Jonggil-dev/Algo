from collections import deque

def solution(s):
    answer = 0
    s = deque(s)
    
    for _ in range(len(s)):
        if check(s):
            answer += 1
        s.append(s.popleft())

    return answer

def check(s):
    stack = []
    for v in s:
        if v == "[" or v == "{" or v == "(":
            stack.append(v)
        else:
            if stack:
                if v == "]" and stack[-1] == "[" or v == ")" and stack[-1] == "(" or v == "}" and stack[-1] == "{":
                    stack.pop()
                    continue
            return False
    
    return not stack