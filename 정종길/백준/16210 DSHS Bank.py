import sys

n = int(sys.stdin.readline().rstrip())
x_li = []
y_li = []
min_distance = 1e9
coordinates = []

for _ in range(n):
    coordinate = list(map(int, sys.stdin.readline().rstrip().split()))
    coordinates.append(coordinate)
    x_li.append(coordinate[0])
    y_li.append(coordinate[1])

x_li.sort()
y_li.sort()

sumx = [0] * (n + 1)
sumy = [0] * (n + 1)
for i in range(n):
    sumx[i + 1] = sumx[i] + x_li[i]
    sumy[i + 1] = sumy[i] + y_li[i]

minv = float('inf')
idx = 0
for i in range(n):
    xi = x_li.index(coordinates[i][0])
    yi = y_li.index(coordinates[i][1])

    sumxx = sumx[n] - sumx[xi + 1] - sumx[xi] + coordinates[i][0] * (xi) - coordinates[i][0] * (n - 1 - xi)
    sumyy = sumy[n] - sumy[yi + 1] - sumy[yi] + coordinates[i][1] * (yi) - coordinates[i][1] * (n - 1 - yi)

    if minv > sumxx + sumyy:
        minv = sumxx + sumyy
        idx = i

print(idx + 1)