def solution(number, k):
    answer = ''
    stack = []
    cnt = 0
    f = 0
    for i in number:
        if f:
            stack.append(i)
        else:
            if not stack or stack[-1] > i:
                stack.append(i)
            else:
                while stack[-1] < i:
                    stack.pop()
                    cnt += 1
                    if cnt >= k:
                        f = 1
                        break
                    if not stack:
                        break
                stack.append(i)
    if cnt < k:
        for _ in range(k-cnt):
            stack.pop()
    answer = "".join(stack)
    return answer
