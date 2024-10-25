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
        # 특정 커서에서 특정 
        cache = {}
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
            answer = min(answer, check_key_cnt(orders, r, c, board))

            
    return answer


def check_key_cnt(orders, r, c, board):
    global answer
    
    copy_board = copy.deepcopy(board)
    cnt = bfs(orders[0], (r, c), copy_board)

    for i in range(len(orders) - 1):
        # 현재 커서에서 orders[i] 카드 까지의 최단거리 계산
        cnt += bfs(orders[i + 1], orders[i], copy_board)
        # 최소 키 조작 횟수 보다 지금 횟수가 더 클 경우 더 이상 볼 필요 없음
        if cnt >= answer:
            return 1e9
    return cnt

def bfs(target, start, board):
    key_cnt = [[0] * 4 for _ in range(4)]
    key_cnt[start[0]][start[1]] = 1
    q = deque([(start[0], start[1])])
    while q:
        x, y = q.popleft()
        if (x, y) == target:
            break
            
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            shift_move(x, y, dx, dy, board, key_cnt, q)
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not key_cnt[nx][ny]:
                    key_cnt[nx][ny] = key_cnt[x][y] + 1
                    q.append((nx, ny))
                    
    board[target[0]][target[1]] = 0
    return key_cnt[target[0]][target[1]]

def shift_move(x, y, dx, dy, board, key_cnt, q):
    cnt = key_cnt[x][y]
    nx, ny = x, y
    while True:
        nx += dx
        ny += dy
        if not (0 <= nx < 4 and 0 <= ny < 4):
            # 가장자리로 이동한 경우
            nx -= dx
            ny -= dy
            if not key_cnt[nx][ny]:
                key_cnt[nx][ny] = cnt + 1
                q.append((nx, ny))
            break
        if board[nx][ny]:
            if not key_cnt[nx][ny]:
                key_cnt[nx][ny] = cnt + 1
                q.append((nx, ny))
            break