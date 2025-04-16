'''
※ 해당 코드는 시간초과 나는 코드임 -> 정답은 2회독 코드 보기
 -> 어디를 캐싱 해야 될 지는 알겠는데 구조상 어떻게 반영해야 될 지 모르겠음

1. 카드를 획득하는 순서 만들기 -> 6! * 2^6
2. 카드별 bfs로 다음 카드까지 최단 거리 구하기 -> 16
'''

from itertools import permutations
from collections import defaultdict, deque
import copy

def solution(board, r, c):
    answer = 1e9
    cards = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cards[board[i][j]].append((i, j))

    n = len(cards)
    for per in permutations(range(1, n + 1), n):
        cache = {}
        for i in range(1 << n):
            orders = deque()
            for num in per:
                if i & (1 << (num - 1)):
                    orders.append(cards[num][0])
                    orders.append(cards[num][1])
                else:
                    orders.append(cards[num][1])
                    orders.append(cards[num][0])

            answer = min(answer, card_matching(orders, board, answer, r, c, cache))
            
    return answer
        

def card_matching(orders, board, answer, r, c, cache):
    
    q = deque([(r, c, 0)])
    target = orders.popleft()
    c_board = copy.deepcopy(board)
    visited = [[-1] * 4 for _ in range(4)]

    while q:
        i, j, cnt = q.popleft()
        
        if cnt >= answer:
            return 1e9
        
        if (i, j) == target:            
            if not orders:
                return cnt + 1

            target = orders.popleft()
            c_board[i][j] = 0
            visited = [[-1] * 4 for _ in range(4)]
            q = deque()
            cnt += 1
            
            
        visited[i][j] = cnt
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < 4 and 0 <= nj < 4 and visited[ni][nj] == -1:
                q.append((ni, nj, cnt + 1))

            ci, cj = ctrl_move(i, j, di, dj, c_board)
            if visited[ci][cj] == -1:
                q.append((ci, cj, cnt + 1))
                

def ctrl_move(i, j, di, dj, c_board):
    
    ni, nj = i + di, j + dj
    while 0 <= ni < 4 and 0 <= nj < 4:
        
        if c_board[ni][nj]:
            return (ni, nj)
        
        ni += di
        nj += dj
        
    return (ni - di, nj - dj)
    