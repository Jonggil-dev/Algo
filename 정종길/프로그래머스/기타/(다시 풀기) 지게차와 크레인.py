'''
1. 지게차랑 크레인이랑 제거 조건이 다름 : states로 지게차를 통해 지울 수 있는지 관리

- 지게차 : 가생이에 있어야 삭제 가능 -> states 확인 후 True인 경우만 삭제
  -> storage 문자 지우기 
  -> 인접 원소가 비어있지 않다면 인접원소 states True로 바꾸기
  -> 인접 원소가 비어있다면, 해당 원소의 인접 원소까지 states True 로 바꾸기

- 크레인 : 우선 무조건 삭제 가능 -> 먼저 삭제 후, 남은 배열에 대해 states와 storage 갱신
  -> storage 문자 지우기 
  -> 지운 원소가 states True 인경우
    -> 인접 원소가 비어있지 않다면 인접원소 states True로 바꾸기
    -> 인접 원소가 비어있다면, 해당 원소의 인접 원소까지 states True 로 바꾸기
'''

def solution(storage, requests):
    global n, m, answer, states
    n, m = len(storage), len(storage[0])
    answer = n * m
    storage = [list(row) for row in storage]
    states = [[False] * m for _ in range(n)]
    states[0] = states[-1] = [True] * m

    for i in range(1, n - 1):
        for j in [0, -1]:
            states[i][j] = True

    for request in requests:
        if len(request) == 1:
            lift(storage, request)
        else:
            crain(storage, request)
    return answer

def lift(storage, request):
    global n, m, answer, states
    candidates = []
    for x in range(n):
        for y in range(m):
            if storage[x][y] == request and states[x][y]:
                candidates.append((x, y))
                answer -= 1

    for x, y in candidates:
        update(x, y, storage)
    return

def crain(storage, request):
    global n, m, answer, states
    alpha = request[0]
    candidates = []
    for x in range(n):
        for y in range(m):
            if storage[x][y] == alpha:
                candidates.append((x, y))
                answer -= 1

    for x, y in candidates:
        update(x, y, storage)
    return

def update(x, y, storage):
    global n, m, states
    storage[x][y] = 0
    if not states[x][y]:
        return
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if storage[nx][ny] != 0 and not states[nx][ny]:
                states[nx][ny] = True
            elif storage[nx][ny] == 0 and not states[nx][ny]:
                states[nx][ny] = True
                update(nx, ny, storage)
    return

