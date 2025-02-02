def solution(n, k, cmd):
    answer = ['O'] * n
    prev = [i - 1 for i in range(n)]
    next_ = [i + 1 for i in range(n)]
    next_[n - 1] = -1
    stack = []       

    for c in cmd:

        if c[0] == 'U':
            x = int(c[2:])
            for _ in range(x):
                k = prev[k]

        elif c[0] == 'D':
            x = int(c[2:])
            for _ in range(x):
                k = next_[k]

        elif c[0] == 'C':
            stack.append(k)
            if prev[k] != -1:
                next_[prev[k]] = next_[k]

            if next_[k] != -1:
                prev[next_[k]] = prev[k]
                k = next_[k]
                
            else:
                k = prev[k]
                
        elif c[0] == 'Z':
            idx = stack.pop()
            if prev[idx] != -1:
                next_[prev[idx]] = idx
            if next_[idx] != -1:
                prev[next_[idx]] = idx

    while stack:
        idx = stack.pop()
        answer[idx] = 'X'
        
    return ''.join(answer)