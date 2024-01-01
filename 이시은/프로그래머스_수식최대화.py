from collections import deque

# 수식의 우선순위가 가능한 모든 경우를 미리 리스트화한 후 순회하면서, 중위표기식을 후위표기식으로 바꾸어 계산한 결과의 절댓값의 최댓값을 구함
def solution(expression):
    op_orders = [['-','*','+'], ['-','+','*'], ['*','-','+'], ['*','+','-'], ['+','*','-'], ['+','-','*']]
    answer = []

    for order in op_orders:
        start = 0
        postfix = deque()
        operators = deque() # stack

        for i in range(len(expression)):
            if not expression[i].isdigit():
                postfix.append(int(expression[start:i]))
                start = i+1
                while operators:
                    op1 = operators[-1]
                    op2 = expression[i]
                    if order.index(op1) <= order.index(op2):
                        postfix.append(operators.pop())
                    else:
                        operators.append(op2)
                        break
                else:
                    operators.append(expression[i])

        postfix.append(int(expression[start:]))
        while operators:
            postfix.append(operators.pop())

        stack = []
        idx = 0
        while idx < len(postfix):
            if type(postfix[idx]) != int:
                a = stack.pop()
                b = stack.pop()
                if postfix[idx] == '+':
                    stack.append(a+b)
                elif postfix[idx] == '-':
                    stack.append(b-a)
                elif postfix[idx] == '*':
                    stack.append(a*b)

            else:
                stack.append(postfix[idx])
            idx += 1

        # print(order)
        # print(postfix)
        # print(stack)
        answer.append(abs(stack[-1]))

    return max(answer)



ep = "100-200*300-500+20"
ep = "50*6-3*2"

print(solution(ep))