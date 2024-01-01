'''
설계
1.그냥 시킨대로 구현하기
'''

from collections import deque

n = int(input())
Arr = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    r,c = map(int,input().split())
    Arr[r-1][c-1] = 1

l = int(input())

input_dir = deque()
for _ in range(l):
    input_dir.append(input().split())

dir = [(0,1), (1,0), (0,-1), (-1,0)]
dir_idx = 0     # dir_idx를 1씩 증가, 감소 시키면서 Right,Left 회전을 구현 (꼬리부분의 이동도 구현하려면 뱀 머리부분과 꼬리부분의 idx를 따로 해야됨)
time = 0        # 게임 시간 초기화
check_idx = 0   # input_dir 체크할 idx

ni = nj = 0 # 현재 위치
q = deque([[0,0]]) # 뱀의 현재 몸통 인덱스들을 기록하는 큐
Arr[ni][nj] = 2

while True:
    time += 1

    if check_idx < l and time - 1 == int(input_dir[check_idx][0]): # ex) input_dir이 [3, "D"]면, 3초까지는 가던방향으로 진행하고 4초 때 바뀐 방향으로 진행하므로 time-1을 비교해야됨
        if input_dir[check_idx][1] == "D":
            dir_idx = (dir_idx + 1) % 4
        else:
            dir_idx = (dir_idx - 1) % 4
        check_idx += 1

    ni += dir[dir_idx][0]
    nj += dir[dir_idx][1]
    q.append([ni,nj])       # 일단 몸통에 추가

    if ni >= n or ni < 0 or nj >= n or nj < 0 or Arr[ni][nj] == 2: # 뱀 머리가 맵을 벗어나거나 몸에 부딪힐 경우
        break

    if Arr[ni][nj] == 1:    # 사과를 밟을 경우
        Arr[ni][nj] = 2     # 몸으로 바꾸기
        continue

    else:                   # 사과가 아닌 경우
        Arr[ni][nj] = 2     # 몸으로 바꾸기
        bi, bj = q.popleft() # 리스트에 맨 먼저 들어갔던게 뱀 꼬리이므로 popleft로 뱀 꼬리 인덱스 추출
        Arr[bi][bj] = 0      # 뱀 꼬리 부분 땅으로 초기화


print(time)