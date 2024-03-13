# Baekjoon 15654번 N과 M(5)

# N개의 자연수 중 M 개를 고른 수열 출력

# 내장함수 사용
from itertools import permutations as perm

N, M = map(int, input().split())
lst = list(map(int, input().split()))

perm_list = sorted(list(perm(lst, M)))
for item in perm_list:
    print(*item)

# 내장함수 사용 X
def DFS(depth):
    if depth == M:
        print(*box)

    for i in range(N):
        if lst[i] in box:
            continue
        box.append(lst[i])
        DFS(depth+1)
        box.pop()

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
box = []
DFS(0)