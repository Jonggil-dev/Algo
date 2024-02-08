from collections import deque

answer = 0
n = int(input())
q = deque()
for i in range(n*2):
    if i < n:
        q.append(input())
    else:
        out = input()
        if out != q[0]:
            q.remove(out)
            answer += 1
        else:
            q.popleft()
print(answer)
