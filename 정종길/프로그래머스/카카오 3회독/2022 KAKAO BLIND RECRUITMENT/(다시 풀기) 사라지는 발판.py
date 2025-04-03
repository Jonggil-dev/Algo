'''
1. 완전 탐색으로 풀기
2. 연산 횟수 파악
-> 5 * 5 board 에서 양쪽 모서리 끝에 A, B 가 위치한다고 가정
-> 보통 이동 경로는 현재 칸에서 2 or 3 방향으로 이동 가능
-> 가장 빨리 끝나는 방향 : 8턴  vs 바장 오래 끝나는 방향 : 25턴 다쓰기
-> 대충 러프하게 평균적으로 3 방향으로 이동가능 + 16턴 쓴다고 치면 -> 4천만
'''
def solution(board, aloc, bloc):
    global r, c
    r, c = len(board), len(board[0])
    answer, _ = dfs(board, [aloc, bloc], 0)
    return answer

def dfs(board, loc, turn):
    global r, c
    
    x, y = loc[turn]
    min_win, max_lose = 25, 0
    
    if board[x][y] == 0:
        return (0, False)

    board[x][y] = 0
    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny]:
                now = True
                loc[turn] = [nx, ny]
                cnt, res = dfs(board, loc, (turn + 1) % 2)
    
                if not res:
                    min_win = min(cnt + 1, min_win)
                else:
                    max_lose = max(cnt + 1, max_lose)
                loc[turn] = [x, y]
    
    board[x][y] = 1
    
    if min_win < 25:
        return (min_win, True)
    else:
        return (max_lose, False)