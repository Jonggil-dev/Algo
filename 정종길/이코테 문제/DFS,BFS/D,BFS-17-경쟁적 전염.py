'''
1. bfs로 구현
2. 맨 처음에만 리스트를 바이러스숫자 기준으로 정렬하면 어짜피 다음 탐색순서는 bfs의 동작과정에 따라(너비우선탐색이므로) 바이러스 숫자가 작은 순서먼저 탐색되게 되어있음
'''
from collections import deque

def virus(i,j,L):
    for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
        ni, nj = i+di, j+dj
        if ni >= 0 and ni < N and nj >= 0 and nj < N:
            if not Arr[ni][nj]:
                Arr[ni][nj] = Arr[i][j]
                q.append((Arr[ni][nj],L+1,ni,nj))
    return

def bfs(S,X,Y):
    while q:
        vir,L,i,j = q.popleft() #L은 시간초를 확인하기 위함
        if L == S:  #시간초 다 된 원소와 처음으로 만날 시 결과 return
            return Arr[X-1][Y-1]
        virus(i, j, L)


N, K = map(int, input().split())
Arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())  # S초 뒤에 X, Y의 바이러스 출력
q= []

for i in range(N):
    for j in range(N):
        if Arr[i][j]:
            q.append((Arr[i][j],0,i,j))

q.sort(key=lambda x:x[0]) # 맨처음 원소들은 vir 숫자 크기순서대로 오름차순 정렬 되어 있어야 함
q = deque(q) #bfs를 위해 리스트를 queue로 변환

res = bfs(S,X,Y)
print(res)