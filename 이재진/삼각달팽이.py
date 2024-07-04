from collections import deque
def solution(n):
    answer = []
    ls = []
    for i in range(1,n+1):
        ls.append(deque([-1])*i)
    dic = {0: [1,0], 1:[0,1], 2: [-1,-1]}
    if n%2 == 0:
        last = (n+1) * (n//2)
    else:
        last = (n+1) * (n//2) + (n//2+1)
    
    ci, cj = 0,0
    dir = 0
    for i in range(1, last+1):
        ls[ci][cj] = i
        ni, nj = ci+dic[dir][0], cj+dic[dir][1]
        if 0<=ni<n and 0<=nj<n and ls[ni][nj] == -1:
            ci, cj = ni, nj
        else:
            dir = (dir+1) % 3
            ci, cj = ci+dic[dir][0], cj+dic[dir][1]
    for i in ls:
        while i:
            answer.append(i.popleft())
    return answer
