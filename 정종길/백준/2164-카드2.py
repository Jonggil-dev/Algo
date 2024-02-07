from collections import deque
N = int(input())
Arr = deque(range(1,N+1))

while len(Arr) > 1:
    Arr.popleft()
    Arr.append(Arr.popleft())

print(Arr[0])
