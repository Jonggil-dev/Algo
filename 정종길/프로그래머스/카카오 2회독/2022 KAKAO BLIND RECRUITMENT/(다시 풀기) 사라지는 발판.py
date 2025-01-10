'''
1. 알고리즘 해설 -> https://dalcheonroadhead.tistory.com/488
  -> 트리 형태로 생각하는게 편함
  -> 요약하면, A부터 시작하는게 고정이니 Depth에 따라 누구 turn인지 결정이됨
  -> 모든 경우의 수에 대해 먼저 깊이를 끝까지 가서 승부를 확인
  -> 끝에서 부터 승부 결과를 상위 노드로 리턴(!!이 때 리턴하는 승부는 최선의 선택으로!!)
  -> 예를 들면 5depth A turn 에서 승, 패, 패 ,승 결과가 있으면 A는 당연히 가장 짧은 승의 경우를 선택해야됨
        -> 4depth B turn 에서는 A의 승리가 넘어 온 것이므로 B의 패배로 반영
        -> 이렇게 다시 4depth B turn 에서 승, 패, 패, 패 가 있으면 B는 당연히 승을 고를 거임 
        -> B가 승을 고르면, 패가 넘어온 하위 노드들은 무시가 됨
        
  -> 이렇게 다시 4dpeth 최상의 노드인 A Turn으로 올라오면 승,패,승,패 등 결과가 있을 것 
    -> 승이 있다면 가장 짧은 승, 패 밖에 없다면 가장 긴 패를 고르면 됨
대충 알고리즘 자체는 이런 흐름임

3. 코드는 유튜브 스윗지니 참고 
'''

def solution(board, aloc, bloc):
    global r, c
    r, c = len(board), len(board[0])
    _, answer = play(board, aloc[0], aloc[1], bloc[0], bloc[1])
    return answer

def play(board, r1, c1, r2, c2):
    if board[r1][c1] == 0:
        return False, 0
    board[r1][c1] = 0
    min_w = 1e9
    max_l = 0
    for dr, dc in (-1, 0), (0, 1), (1, 0), (0, -1):
        nr, nc = r1 + dr, c1 + dc
        if 0 <= nr < r and 0<= nc < c and board[nr][nc] == 1:
            lose, cnt = play(board, r2, c2, nr, nc)
            if lose:
                max_l = max(max_l, cnt + 1)
            else:
                min_w = min(min_w, cnt + 1)
    board[r1][c1] = 1
    if min_w < 1e9:
        return True, min_w
    else:
        return False, max_l
            