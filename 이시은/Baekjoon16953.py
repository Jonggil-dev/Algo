# baekjoon16953 A -> B

import sys

input = sys.stdin.readline

start, end = map(int, input().split())

MIN = float("inf")
def DFS(n, cnt):
    global MIN
    if n == end:
        MIN = min(MIN, cnt)
        return

    if n > end:
        return

    DFS(n * 2, cnt + 1)
    DFS(int(str(n) + '1'), cnt+1)

DFS(start, 1)

if MIN == float("inf"):
    print(-1)

else:
    print(MIN)