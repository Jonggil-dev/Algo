def solution(p):

    if not p:
        return p

    u, v = divide(p)

    if is_valid(u):
        return u + solution(v)
    
    new_string = '(' + solution(v) + ')'
    
    return new_string + reverse(u[1:-1])

def divide(p):
    left = right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i + 1], p[i + 1:]

def is_valid(p):
    stack = []
    for char in p:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
            
    return not stack

def reverse(p):
    return ''.join('(' if char == ')' else ')' for char in p)
