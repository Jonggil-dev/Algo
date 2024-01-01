from collections import deque
import sys
N = int(sys.stdin.readline())
q = deque()
a, b = 0, float('inf')
idx = -1
for _ in range(N):
    x = sys.stdin.readline().split()
    if x[0] == '1':
        q.append(int(x[1]))
        idx += 1
    elif x[0] == '2':
        q.popleft()
        idx -= 1
    if a < idx:
        a = idx
        b = q[idx]
    elif a == idx:
        if b > q[idx]:
            b = q[idx]
print(a+1, b)
