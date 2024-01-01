'''
설계
1. 그룹을 나타내는 인덱스 배열을 만들어서 동일 그룹여부 확인하기
2. i,j 전체 순회를 while문 안으로 넣어서 전체 그룹화가 끝나면 처음부터 다시 그룹화가 가능한지 확인하도록 로직작성
'''

from collections import deque
from pprint import pprint

#특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def bfs(x,y,index):
    # (x,y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x,y))
    # 너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
    q = deque()
    q.append((x,y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = Arr[x][y] # 현재 연합의 전체 인구 수
    cnt = 1 # 현재 연합의 국가 수

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(Arr[x][y] - Arr[nx][ny]) <= r:
                    q.append((nx,ny))
                    #연합에 추가
                    union[nx][ny] = index
                    summary += Arr[nx][ny]
                    cnt += 1
                    united.append((nx,ny))
    #연합 국가끼리 인구 분배
    for i, j in united:
        Arr[i][j] = summary//cnt
    return

n,l,r = map(int,input().split())
Arr= [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

res = 0
# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                bfs(i,j,index)
                index += 1

    # 모든 인구 이동이 끝난 경우
    if index == n*n:
        break
    res += 1

print(res)