
from collections import deque

def vaild_check(i,j):
    if i < 0 or N <= i or j < 0 or N <= j :
        return False

    if (i,j) in tracks:
        return False
    return True

def snake():
    time = 0
    i = j = direction = 0
    dir = 0
    di, dj = delta[direction]
    while True:
        time += 1
        i, j = i + di, j + dj
        if not vaild_check(i,j):
            return time

        tracks.append((i, j))
        if Arr[i][j] == 1:
            Arr[i][j] = 0
        elif Arr[i][j] == 0:
            tracks.popleft()

        if dir < L and time == changes[dir][0]:
            if changes[dir][1] == "D":
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
            dir += 1
            di, dj = delta[direction]

N = int(input())
K = int(input())
Arr = [[0] * N for _ in range(N)]
apples = []
changes = deque()
tracks = deque([(0,0)])

delta = [(0,1),(1,0),(0,-1),(-1,0)]

for _ in range(K):
    r,c = map(int,input().split())
    Arr[r-1][c-1] = 1


L = int(input())
for _ in range(L):
    time, text = input().split()
    changes.append((int(time),text))

res = snake()
print(res)