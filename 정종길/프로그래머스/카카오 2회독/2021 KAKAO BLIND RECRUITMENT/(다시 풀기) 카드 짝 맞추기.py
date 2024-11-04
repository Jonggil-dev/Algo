from itertools import permutations
from collections import defaultdict, deque
import copy

def solution(board, r, c):
    global answer
    
    answer = 1e9
    cards = defaultdict(list)
    
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cards[board[i][j]].append((i, j))
    
    n = len(cards)
    #모든 경우의 수 탐색
    for per in permutations(cards.keys(), n):
        # 시간 줄이기 위해 캐시 사용
        # 어짜피 수집하는 key의 순서는 정해져 있고, 해당 key내에서 2개중 어떤걸 먼저 선택하는지 탐색하는 부분이므로, A -> B로 가는 경로 내에 특정 카드가 있었다가 뒤집혀서 없어졌다가 하는 경우는 없음!! -> 아래 캐시 사용의 근거 
        cache = defaultdict(int)
        #카드 번호 별로 2가지 카드가 있으므로 하나의 per에 대해 2 ** n 만큼 수집 순서가 있음
        for case in range(1 << n):
            # 카드 수집 순서를 담기 위한 orders
            orders = []
            for card_num in per:
                num_cards = cards[card_num]
                if case & (1 << (card_num - 1)):
                    orders.append(num_cards[0])
                    orders.append(num_cards[1])
                else:
                    orders.append(num_cards[1])
                    orders.append(num_cards[0])
                    
            # orders에 per에 대한 1개의 순서가 정해졌으므로 키 조작 횟수 계산
            answer = min(answer, check_key_cnt(orders, r, c, board, cache))
    
    return answer

def check_key_cnt(orders, r, c, board, cache):
    copy_board = copy.deepcopy(board)
    cnt = 0
    current_pos = (r, c)
    for target in orders:
        move_cnt = bfs(current_pos, target, copy_board, cache)
        cnt += move_cnt
        # 카드 뒤집기
        copy_board[target[0]][target[1]] = 0
        current_pos = target
    return cnt


def bfs(start, target, board, cache):
    if start == target:
        return 1  # 'Enter' 키 입력만 필요하므로 1 반환

    if cache[(start, target)]:
        return cache[(start, target)] + 1
    
    key_cnt = [[-1] * 4 for _ in range(4)]
    key_cnt[start[0]][start[1]] = 0
    q = deque()
    q.append((start[0], start[1]))

    while q:
        x, y = q.popleft()
        if (x, y) == target:
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # 일반 이동
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                if key_cnt[nx][ny] == -1 or key_cnt[nx][ny] > key_cnt[x][y] + 1:
                    key_cnt[nx][ny] = key_cnt[x][y] + 1
                    q.append((nx, ny))
                    
            # 컨트롤 이동
            nx_ctrl, ny_ctrl = ctrl_move(x, y, dx, dy, board)
            if key_cnt[nx_ctrl][ny_ctrl] == -1 or key_cnt[nx_ctrl][ny_ctrl] > key_cnt[x][y] + 1:
                key_cnt[nx_ctrl][ny_ctrl] = key_cnt[x][y] + 1
                q.append((nx_ctrl, ny_ctrl))
                
    cache[(start, target)] = key_cnt[target[0]][target[1]]
    return key_cnt[target[0]][target[1]] + 1  # 'Enter' 키 입력 포함

def ctrl_move(x, y, dx, dy, board):
    nx, ny = x, y
    while True:
        nx += dx
        ny += dy
        if not (0 <= nx < 4 and 0 <= ny < 4):
            nx -= dx
            ny -= dy
            break
        if board[nx][ny]:
            break
    return nx, ny
    