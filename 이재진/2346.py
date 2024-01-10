from collections import deque

n = int(input())
balloons = deque(enumerate(map(int, input().split()), start=1))
result = []

while balloons:
    index, move = balloons.popleft()
    result.append(index)

    if move > 0:
        balloons.rotate(-(move - 1))
    else:
        balloons.rotate(-move)

print(' '.join(map(str, result)))
