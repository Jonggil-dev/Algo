def solution(s):
    stack = []

    for txt in s:
        if stack:
            if stack[-1] == txt:
                stack.pop()
                continue

        stack.append(txt)

    if stack:
        answer = 0
    else:
        answer = 1

    return answer