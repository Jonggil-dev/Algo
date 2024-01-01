func = input()
result = ''
stack = [0] * 100
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
for i in func:
    if i not in '(+-*/)':
        result += i
    elif i == ')':
        while stack[top] != '(':
            result += stack[top]
            top -= 1
        top -= 1
    else:
        if top == -1 or isp[stack[top]] < icp[i]:
            top += 1
            stack[top] = i
        else:
            while top > -1 and isp[stack[top]] >= icp[i]:
                result += stack[top]
                top -= 1
            top += 1
            stack[top] = i

while top != -1:
    result += stack[top]
    top -= 1

print(result)
